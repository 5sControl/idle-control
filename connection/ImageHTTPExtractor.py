import httplib2
import logging
import datetime
import numpy as np
import cv2
from typing import Tuple, Union
import socketio


sio = socketio.AsyncClient()
images = {}


class ImageHTTPExtractor:
    def __init__(self, camera_ip: str, logger: logging.Logger, **credentials) -> None:
        self.http_connection = httplib2.Http(".cache")
        self.http_connection.add_credentials(credentials.get("username"), credentials.get("password"))
        self.logger = logger
        self.camera_ip = camera_ip

    def get_snapshot(self) -> Tuple[Union[cv2.Mat, None], Union[datetime.time, None]]:
        try:
            global images
            image = images[self.camera_ip]            
            curr_time = datetime.datetime.now()
            nparr = np.frombuffer(image, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            return img, curr_time
        except Exception as exc:
            self.logger.warning(f"Cannot retrieve image. Following error raised - {exc}")
            print(images.keys())
            return None, None

@sio.event
async def connect():
    print("Connection")

@sio.event
async def snapshot_updated(data):
    camera_ip, screen = data.get("camera_ip"), data.get("screenshot")
    print(f"Image on {camera_ip} was updated")
    global images
    images[camera_ip] = screen

async def run_sio(url):
    await sio.connect(url)
    await sio.wait()
