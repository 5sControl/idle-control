from confs.load_configs import *
import os
import uuid
import datetime
import pathlib
import logging
import colorlog
import cv2
import requests
import httplib2
import numpy as np
from idle_models.IdleObjectDetectionModel import IdleObjectDetectionModel
import time
from dotenv import load_dotenv


def create_logger():
    logger = logging.getLogger('min_max_logger')
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'CRITICAL': 'bold_red,bg_white',
        }))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    return logger


def init_connection():
    password = os.environ.get("password")
    if password is None:
        load_dotenv("confs/settings.env")
        password = os.environ.get("password")
    username = os.environ.get("username")
    try:
        h = httplib2.Http(".cache")
        h.add_credentials(username, password)
        return h
    except Exception as exc:
        logging.error('init connection:\n' + str(exc))
    return None


def init_model():
    model = IdleObjectDetectionModel(
        MODEL_PATH,
        CONF_THRES,
        IOU_THRES,
        CLASSES
    )
    return model


def get_frame(h):
    try:
        time_ = datetime.datetime.now()
        _, content = h.request(os.environ.get(
            "camera_url"), "GET", body="foobar")
        nparr = np.frombuffer(content, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img, time_
    except Exception as exc:
        return None, None


def put_rectangle(img, boxes, scores):
    for (x1, y1, x2, y2), score in zip(boxes.astype(int), scores):
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(img, str(score), (x1, y1),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    return img


def check_coordinates_diffs(coords_1: np.array, coords_2: np.array, threshold=THRESHOLD):
    if coords_1 is None:
        return True
    diff = np.abs(coords_1 - coords_2).sum()
    return diff > threshold


def send_report_and_save_photo(img0, start_track_time):
    server_url = os.environ.get("server_url")
    folder = os.environ.get("folder")

    pathlib.Path(folder).mkdir(exist_ok=True, parents=True)
    save_photo_url = f'{folder}/' + str(uuid.uuid4()) + '.jpg'
    cv2.imwrite(save_photo_url, img0)

    time.sleep(WAIT_TIME)
    stop_tracking = str(datetime.datetime.now())

    report_for_send = {
        'camera': folder.split('/')[1],
        'algorithm': 'idle_control',
        'start_tracking': start_track_time,
        'stop_tracking': stop_tracking,
        'photos': [{'image': save_photo_url, 'date': start_track_time}],
        'violation_found': True,
    }
    try:
        requests.post(
            url=f'{server_url}:80/api/reports/report-with-photos/', json=report_for_send)
    except Exception as exc:
        logging.error('send report:\n' + str(exc))
