import requests
import numpy as np
from logging import Logger
from PIL import Image
import io


PORT = 5001


def convert_image2bytes(image: np.array, format='PNG', encoding='utf-8'):
    pil_image = Image.fromarray(image)
    img_byte_arr = io.BytesIO()
    pil_image.save(img_byte_arr, format=format)
    img_byte_arr.seek(0)
    return img_byte_arr


def predict(img: np.array, server_url: str, logger: Logger) -> list:
    try:
        response = requests.post(
            f"{server_url}:{PORT}/predict",
            files={
                  "image": ("image", convert_image2bytes(img), "image/png")
            }
        )
        response.raise_for_status()
        return np.array(response.json().get("coordinates"))
    except Exception as exc:
        logger.critical("Cannot send request. Error - {}".format(exc))
