import torch
from yolor.model import get_model
import numpy as np
from yolor.utils.datasets import letterbox
from yolor.utils.general import non_max_suppression, scale_coords


class IdleObjectDetectionModel:
    def __init__(self, path: str, conf_thresh, iou_thresh, classes, conf_path) -> None:
        self.model, self.device = get_model(path, conf_path)
        self.conf_thresh = conf_thresh
        self.iou_thresh = iou_thresh
        self.classes = classes

    def __preprocess_image(self, img: np.array) -> np.array:
        self.img_shape = img.shape
        img = letterbox(img.copy(), new_shape=1280, auto_size=64)[0]
        img = img[:, :, ::-1].transpose(2, 0, 1)
        img = np.ascontiguousarray(img)
        img = torch.from_numpy(img).to(self.device)
        img = img.float()
        img /= 255.0
        img = img.unsqueeze(0)
        return img

    @torch.no_grad()
    def __call__(self, img: np.array) -> list:
        img = self.__preprocess_image(img)
        pred = self.model(img, augment=False)[0]
        pred = non_max_suppression(
            pred, 0.45, 0.5, classes=[67], agnostic=False)[0]
        pred[:, :4] = scale_coords(
            img.shape[2:], pred[:, :4], self.img_shape).round()
        return pred[:, :4], pred[:, 4]
