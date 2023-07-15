import torch
import numpy as np
from transformers import DetrImageProcessor, DetrForObjectDetection
import torch


class IdleObjectDetectionModel:
    def __init__(self, path: str, conf_thresh, iou_thresh, classes) -> None:
        self.model = DetrForObjectDetection.from_pretrained(path)
        self.model.eval()
        self.processor = DetrImageProcessor.from_pretrained(path)
        self.conf_thresh = conf_thresh
        self.iou_thresh = iou_thresh
        self.classes = classes

    @torch.no_grad()
    def __call__(self, img: np.array) -> np.array:
        inputs = self.processor(images=img, return_tensors="pt")
        outputs = self.model(**inputs)
        target_sizes = torch.tensor([img.shape[:-1]])
        results = self.processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=self.conf_thresh)[0]
        pred = []
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            if self.model.config.id2label[label.item()] == 'cell phone':
                pred.append([round(i, 2) for i in box.tolist()] + [score.item()])
        return np.array(pred)
