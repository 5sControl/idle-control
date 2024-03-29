import cv2
import numpy as np
import numba
import os
import uuid


def put_rectangle(img: cv2.Mat, boxes: list, scores: list) -> np.array:
    for (x1, y1, x2, y2), score in zip(boxes.astype(int), scores):
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), 2)
        cv2.putText(img, str(round(score, 3)), (x1, y1),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    return img


@numba.njit(numba.boolean(numba.float32[:, :], numba.float32[:, :], numba.float32), parallel=True)
def bboxes_not_equal(coords_1: np.array, coords_2: np.array, threshold: float) -> bool:
    if coords_1 is None or coords_1.shape != coords_2.shape:
        return True
    return np.abs(coords_1 - coords_2).sum() > threshold

def save_cropped_bbox(img: np.array, bboxes: np.array):
    os.makedirs("images/debug/", exist_ok=True)
    try:
        for bbox in bboxes:
            x1, y1, x2, y2 = bbox.astype(int)
            c = 15
            cv2.imwrite(f"images/debug/{uuid.uuid4()}.png", img[x1 - c:x2 + c, y1 - c:y2 + c])
    except Exception:
        pass