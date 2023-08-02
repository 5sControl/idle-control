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

    def predict(self, img: np.array) -> np.array:
        try:
            response = requests.post(
                f"{self.server_url}:{PORT}/predict",
                files={
                    "image": ("image", self._convert_image2bytes(img), "image/png")
                }
            )
            response.raise_for_status()
            return np.array(response.json().get("coordinates")).astype(np.float32)
        except Exception as exc:
            self.logger.critical("Cannot send request to model server. Error - {}".format(exc))
            return np.array([[]])
