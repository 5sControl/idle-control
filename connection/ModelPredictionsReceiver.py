import requests
import numpy as np
from logging import Logger
from PIL import Image
import io


PORT = 5001


class ModelPredictionsReceiver:
    def __init__(self, server_url: str, logger: Logger) -> None:
        self.server_url = server_url
        self.logger = logger

    @staticmethod
    def _convert_image2bytes(image: np.array, format='PNG') -> io.BytesIO:
        pil_image = Image.fromarray(image)
        img_byte_arr = io.BytesIO()
        pil_image.save(img_byte_arr, format=format)
        img_byte_arr.seek(0)
        return img_byte_arr

    def _predict(self, img: np.array) -> np.array:
        try:
            response = requests.post(
                f"{self.server_url}:{PORT}/predict",
                files={
                    "image": ("image", self._convert_image2bytes(img), "image/png")
                }
            )
            response.raise_for_status()
            return np.array(response.json().get("coordinates"))
        except Exception as exc:
            self.logger.critical("Cannot send request to model server. Error - {}".format(exc))
            return np.array([])

    def predict(self, img: np.array) -> np.array:
        imgs = [
            img[:img.shape[0] // 2, :, :],
            img[img.shape[0] // 2:, :, :]
        ]
        preds = [self._predict(imgs[0]), self._predict(imgs[1])]
        print(preds)
        if len(preds[1]):
            preds[1][:, 1] += img.shape[0] // 2
            preds[1][:, 3] += img.shape[0] // 2
        result = np.append(*preds)
        if len(result.shape) == 1:
            result = np.expand_dims(result, 0)
        print(result.shape)
        print(result)
        return result
