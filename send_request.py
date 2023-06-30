import requests
import numpy as np
from logging import Logger


PORT = 5001


def predict(img: np.array, server_url: str, logger: Logger):
    response = requests.post(
        f"{server_url}:{PORT}/predict",
        json={
            "image": img.tolist()
        }
    )
    if response.status_code == 200:
        coordinates = np.array(response.json().get("coordinates"))
        confidences = np.array(response.json().get("confidences"))
    else:
        logger.warning(
            "Status code = {}\n response = {}".format(
                response.status_code, response)
        )
        coordinates = confidences = None
    return [coordinates, confidences]
