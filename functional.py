
import os
import uuid
import datetime
import pathlib

import cv2
import torch
import yolov7
import requests
import httplib2
import numpy as np


def init_connection():
    password =  os.environ.get("password")
    username =  os.environ.get("username")
    
    try:
        h = httplib2.Http(".cache")
        h.add_credentials(username, password)
        return h
    except Exception as exc:
        print(exc)

    return None


def init_model():
    model = yolov7.load('yolov7x.pt')

    # set model parameters
    model.conf = 0.15  # NMS confidence threshold
    model.iou = 0.45  # NMS IoU threshold
    model.classes = [67]  # (optional list) filter by class
    return model


def get_frame(h):
    try:
        resp, content = h.request(os.environ.get("camera_url"), "GET", body="foobar")
        if resp.status == 200: # TODO: check if this condition can be false at all
            nparr = np.frombuffer(content, np.uint8)
            img0 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            return img0
    except Exception as exc:
        print(exc)
    return None


@torch.no_grad()
def predict(model, img):
    results = model(img)
    predictions = results.pred[0].cpu().detach().numpy()
    boxes = predictions[:, :4]  # x1, y1, x2, y2 # TODO: check numpy.split and get something like boxes,scores,cats = np.split(...
    scores = predictions[:, 4]
    categories = predictions[:, 5]
    return boxes, scores, categories


def put_rectangle(img, boxes, scores):
    for (x1, y1, x2, y2), score in zip(boxes.astype(int), scores):
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(img, str(score), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    return img


def send_report_and_save_photo(img0):
    camera_url = os.environ.get("camera_url")
    server_url =  os.environ.get("server_url")
    folder =  os.environ.get("folder")

    pathlib.Path(folder).mkdir(exist_ok=True, parents=True)
    save_photo_url = f'{folder}/' + str(uuid.uuid4()) + '.jpg'
    cv2.imwrite(save_photo_url, img0)
    photo_date = str(datetime.datetime.now())
    report_for_send = {
                'camera': camera_url,
                'algorithm': 'idle_control',
                'start_tracking': photo_date,
                'stop_tracking': photo_date,
                'photos': [{'image': save_photo_url, 'date': photo_date}],
                'violation_found': True,
            }
    try:
        r = requests.post(url=f'{server_url}:80/api/reports/report-with-photos/', json=report_for_send)
    except Exception as exc:
        print(exc, 'exc')
        pass
    