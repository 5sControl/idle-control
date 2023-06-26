from ultralytics import YOLO
import torch
import numpy as np
from idle_models.IdleObjectDetectionModel import IdleObjectDetectionModel


class IdleObjectDetectionModelPipeline:
    def __init__(self, first_model_path: str, second_model_path: str, conf_thresh: float, iou_thresh: float, classes: list) -> None:
        self.first_model = IdleObjectDetectionModel(
            first_model_path, conf_thresh, iou_thresh, classes)
        self.second_model = IdleObjectDetectionModel(
            second_model_path, conf_thresh, iou_thresh, classes)
        self.conf_thresh = conf_thresh
        self.iou_thresh = iou_thresh
        self.classes = classes

    @torch.no_grad()
    def __call_second_model__(self, img: np.array, coordinates: np.array) -> list:
        drop_indices = []
        for row_index in range(len(coordinates)):
            x1, y1, x2, y2 = list(map(int, coordinates[row_index].tolist()))
            truncated_image = img[x1:x2, y1:y2]
            if len(
                self.second_model(
                    img=truncated_image
                )[1]
            ) > 0:
                drop_indices.append(row_index)
        return drop_indices

    def __drop_elements_from_tensor__(self, tensor: torch.Tensor, indices: list):
        for index in indices:
            tensor = torch.cat([
                tensor[:index],
                tensor[index + 1:]
            ])
        return tensor

    @torch.no_grad()
    def __call__(self, img) -> list:
        coordinates, confidences = self.first_model(
            img=img
        )
        drop_indices = self.__call_second_model__(img, coordinates)
        coordinates = self.__drop_elements_from_tensor__(
            coordinates, drop_indices)
        confidences = self.__drop_elements_from_tensor__(
            confidences, drop_indices)
        return [coordinates, confidences]
