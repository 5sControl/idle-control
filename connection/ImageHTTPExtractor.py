import logging
import datetime
import numpy as np
import cv2
from typing import Tuple, Union
import requests


class ImageHTTPExtractor:
    def __init__(self, camera_ip: str, logger: logging.Logger, **credentials) -> None:
        self.logger = logger
        self.camera_ip = camera_ip

    def get_snapshot(self) -> Tuple[Union[cv2.Mat, None], Union[datetime.time, None]]:
        try:
            response = requests.get(self.camera_ip)  
            curr_time = datetime.datetime.now()
            nparr = np.frombuffer(response.content, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            return img, curr_time
        except Exception as exc:
            self.logger.warning(f"Cannot retrieve image. Following error raised - {exc}")
            return None, None

