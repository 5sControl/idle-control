import torch
import numpy as np
import cv2


class IdleObjectDetectionModel:
    def __init__(self, weights_path: str, conf_path: str, conf_thresh, iou_thresh, classes) -> None:
        self.model = cv2.dnn_DetectionModel(weights_path, conf_path)
        self.model.setInputSize(640, 640)
        self.model.setInputScale(1.0 / 127.5)
        self.model.setInputMean((127.5, 127.5, 127.5))
        self.model.setInputSwapRB(True)
        self.conf_thresh = conf_thresh
        self.iou_thresh = iou_thresh
        self.classes = classes

    @torch.no_grad()
    def __call__(self, img) -> list:
        classIds, confs, bbox = self.model.detect(
            img, confThreshold=self.conf_thresh,
        )
        filter_vals = classIds == 77
        classIds = classIds[filter_vals]
        confs = confs[filter_vals]
        bbox = bbox[filter_vals]
        for idx, row in enumerate(bbox):
            x1, y1, w, h = row.astype(int)
            x2, y2 = x1 + w, y1 + h
            bbox[idx] = [x1, y1, x2, y2]
        return bbox, confs
