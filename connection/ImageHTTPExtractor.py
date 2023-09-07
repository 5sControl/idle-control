import httplib2
import logging
import datetime
import numpy as np
import cv2
from typing import Tuple, Union


class ImageHTTPExtractor:
    def __init__(self, camera_ip: str, logger: logging.Logger, **credentials) -> None:
        self.http_connection = httplib2.Http(".cache")
        self.http_connection.add_credentials(credentials.get("username"), credentials.get("password"))
        self.logger = logger
        self.camera_ip = camera_ip

    def get_snapshot(self) -> Tuple[Union[cv2.Mat, None], Union[datetime.time, None]]:
        try:
            response, content = self.http_connection.request(
                self.camera_ip,
                "GET", 
                body="foobar"
            )        
            curr_time = datetime.datetime.now()
            nparr = np.frombuffer(content, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            return img, curr_time
        except Exception as exc:
            self.logger.warning(f"Cannot retrieve image. Following error raised - {exc}")
            return None, None

