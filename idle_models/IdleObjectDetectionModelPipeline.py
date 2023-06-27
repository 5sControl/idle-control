from ultralytics import YOLO
import torch
import numpy as np
from idle_models.IdleObjectDetectionModel import IdleObjectDetectionModel
import cv2


class IdleObjectDetectionModelPipeline:
    def __init__(self, models: list[IdleObjectDetectionModel]) -> None:
        self.first_model = models[0]

    @torch.no_grad()
    def __call_second_model__(self, img: np.array, coordinates: np.array) -> list:
        drop_indices = []
        for row_index in range(len(coordinates)):
            x1, y1, x2, y2 = list(map(int, coordinates[row_index].tolist()))
            sec_model_preds = self.second_model(img=img)
            # if not len(sec_model_preds[1]) > 0:
            #    drop_indices.append(row_index)
            #    print("drop")
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
        return [coordinates, confidences]
