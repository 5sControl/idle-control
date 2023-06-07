
import os
import uuid
import datetime
import pathlib
import logging

import cv2
import torch
import requests
import httplib2
import numpy as np

from super_gradients.training import models
from super_gradients.common.object_names import Models


def init_connection():
    password =  os.environ.get("password")
    username =  os.environ.get("username")
    try:
        h = httplib2.Http(".cache")
        h.add_credentials(username, password)
        return h
    except Exception as exc:
        logging.error('init connection:\n' + str(exc))
    return None


def init_model():
    model = models.get(Models.YOLO_NAS_M, pretrained_weights="coco")
    return model


def get_frame(h):
    try:
        _, content = h.request(os.environ.get("camera_url"), "GET", body="foobar")
        nparr = np.frombuffer(content, np.uint8)
        img0 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img0
    except Exception as exc:
        logging.error('get frame:\n' + str(exc))
    return None


@torch.no_grad()
def predict(model, img):
    pred = next(model.predict(img)._images_prediction_lst)

    boxes, scores, categories = pred.prediction.bboxes_xyxy.astype(np.uint16), pred.prediction.confidence, pred.prediction.labels.astype(np.uint16)
    mask, = np.where(categories == 67.)
    boxes, scores, categories = boxes[mask], scores[mask], categories[mask]
    return boxes, scores, categories


def put_rectangle(img, boxes, scores):
    for (x1, y1, x2, y2), score in zip(boxes.astype(int), scores):
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(img, str(score), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    return img


def send_report_and_save_photo(img0):
    server_url =  os.environ.get("server_url")
    folder =  os.environ.get("folder")

    pathlib.Path(folder).mkdir(exist_ok=True, parents=True)
    save_photo_url = f'{folder}/' + str(uuid.uuid4()) + '.jpg'
    cv2.imwrite(save_photo_url, img0)

    time_delta_seconds = 10
    start_tracking = str(datetime.datetime.now())
    stop_tracking = str(datetime.datetime.now() + datetime.timedelta(0, time_delta_seconds))

    report_for_send = {
                'camera': folder.split('/')[1],
                'algorithm': 'idle_control',
                'start_tracking': start_tracking,
                'stop_tracking': stop_tracking,
                'photos': [{'image': save_photo_url, 'date': start_tracking}],
                'violation_found': True,
            }
    try:
        requests.post(url=f'{server_url}:80/api/reports/report-with-photos/', json=report_for_send)
    except Exception as exc:
        logging.error('send report:\n' + str(exc))
    