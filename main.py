import utils
from connection import IdleReporter, ImageHTTPExtractor, ModelPredictionsReceiver
from confs import configs
from dotenv import load_dotenv
from IdleAlgorithm import IdleAlgorithm
import os
import numpy as np
import asyncio


password = os.environ.get("password")
if password is None:
    load_dotenv("confs/settings.env")
password = os.environ.get("password")
username = os.environ.get("username")
server_url = os.environ.get("server_url")
camera_ip = os.environ.get("camera_url")
folder = os.environ.get("folder")

logger = utils.create_logger()

prev_preds = np.array([[]]).astype(np.float32)
reporter = IdleReporter(folder, server_url, configs["wait_time"], logger)
image_extractor = ImageHTTPExtractor(camera_ip, logger, username=username, password=password)
model_predictor = ModelPredictionsReceiver(server_url, logger)
algo = IdleAlgorithm(logger, image_extractor, model_predictor, reporter)


algo.start()
