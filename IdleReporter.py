import os
import time
from confs.load_configs import WAIT_TIME
import logging
import requests
import datetime
import uuid
import cv2
import numpy as np


class IdleReporter:
    def __init__(self, images_folder: str, server_url: str) -> None:
        self.images_folder = images_folder
        self.server_url = server_url
        os.mkdir(self.images_folder) if not os.path.exists(self.images_folder) else ...

    def _save_image(self, image: np.array) -> str:
        save_photo_url = f'{self.images_folder}/' + str(uuid.uuid4()) + '.jpg'
        cv2.imwrite(save_photo_url, image)
        return save_photo_url

    def create_report(self, image: np.array, start_tracking_time: datetime.time) -> dict:
        time.sleep(WAIT_TIME)
        stop_tracking_time = str(datetime.datetime.now())
        saved_image_name = self._save_image(image)
        report_for_send = {
            'camera': self.images_folder.split('/')[1],
            'algorithm': 'idle_control',
            'start_tracking': start_tracking_time,
            'stop_tracking': stop_tracking_time,
            'photos': [{'image': saved_image_name, 'date': start_tracking_time}],
            'violation_found': True,
        }
        return report_for_send

    def send_report(self, report: dict):
        try:
            requests.post(
                url=f'{self.server_url}:80/api/reports/report-with-photos/', json=report
            )
        except Exception as exc:
            self.logger.error(f"Cannot send report. Following error raised: {str(exc)}")


