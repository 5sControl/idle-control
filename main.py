import time
import utils
import connection
from confs import configs
from dotenv import load_dotenv
import os
import numpy as np


password = os.environ.get("password")
if password is None:
    load_dotenv("confs/settings.env")
password = os.environ.get("password")
username = os.environ.get("username")
server_url = os.environ.get("server_url")
camera_url = os.environ.get("camera_url")
folder = os.environ.get("folder")

logger = utils.create_logger()

prev_preds = None
reporter = connection.IdleReporter(folder, server_url, configs["wait_time"], logger)
image_extractor = connection.ImageHTTPExtractor(camera_url, logger, username=username, password=password)
model_predictor = connection.ModelPredictionsReceiver(server_url, logger)

iter_idx = 0

while True:
    iter_idx += 1
    if iter_idx % 60 == 0:
        logger.info("60 iterations passed")
    img, start_tracking = image_extractor.get_snapshot()
    if img is None:
        time.sleep(1)
        continue
    preds = model_predictor.predict(img)
    if preds is None:
        time.sleep(1)
        continue
    if preds.size != 0 and np.any(preds[:, -1] == 1.):
        logger.info("Telephone is detected")
        if utils.are_bboxes_equal(prev_preds, preds, configs["threshold"]):
            img = utils.put_rectangle(img, preds[:, :4], preds[:, 4])
            reporter.send_report(reporter.create_report(img, str(start_tracking)))
        prev_preds = preds
    time.sleep(2)
