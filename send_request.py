import requests
import numpy as np


PORT = 5000


def predict(img: np.array, server_url: str):
    response = requests.post(
        f"{server_url}:{PORT}/predict",
        json={
            "image": img.tolist()
        }
    )
    coordinates = np.array(response.json().get("coordinates"))
    confidences = np.array(response.json().get("confidences"))
    return [coordinates, confidences]
