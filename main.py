import os
import yolov7
import numpy as np
import cv2
import httplib2
import time

password = os.environ.get("password")
username = os.environ.get("username")
camera_url = os.environ.get("camera_url")
h = httplib2.Http(".cache")
h.add_credentials(username, password)

model = yolov7.load('yolov7.pt')
# set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.classes = None  # (optional list) filter by class


def run():
    while True:
        time.sleep(1)
        resp, content = h.request(camera_url, "GET", body="foobar")
        if resp.status == 200:
            nparr = np.frombuffer(content, np.uint8)
            img0 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        else:
            print('Error: Could not retrieve image')
            continue

        results = model(img0)
        predictions = results.pred[0]
        boxes = predictions[:, :4]  # x1, y1, x2, y2
        scores = predictions[:, 4]
        categories = predictions[:, 5]
        print(categories, 'categories')

if __name__ == '__main__':
    run()
