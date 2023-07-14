import time
from functional import *
from send_request import predict
from dotenv import load_dotenv
from IdleReporter import IdleReporter
from logger import create_logger
from ImageHTTPExtractor import ImageHTTPExtractor
import os


password = os.environ.get("password")
if password is None:
    load_dotenv("confs/settings.env")
password = os.environ.get("password")
username = os.environ.get("username")
server_url = os.environ.get("server_url")
camera_url = os.environ.get("camera_url")
folder = os.environ.get("folder")

logger = create_logger()


prev_preds = None
reporter = IdleReporter(folder, server_url, logger)
image_extractor = ImageHTTPExtractor(camera_url, logger, username=username, password=password)

iter_idx = 0

while True:
    iter_idx += 1
    if iter_idx % 60 == 0:
        logger.info("60 iterations passed")
    img, start_tracking = image_extractor.get_snapshot()
    if img is None:
        time.sleep(1)
        continue
    preds = predict(img, server_url, logger)
    if preds is None:
        time.sleep(1)
        continue
    if len(preds) > 0:
        logger.info("Telephone is detected")
        if are_bboxes_equal(prev_preds, preds, THRESHOLD):
            img = put_rectangle(img, preds[:, :4], preds[:, 4])
            reporter.send_report(reporter.create_report(img, str(start_tracking)))
        prev_preds = preds
