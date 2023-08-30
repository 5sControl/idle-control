import utils
from connection import run_sio, IdleReporter, ImageHTTPExtractor, ModelPredictionsReceiver
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
camera_ip = os.environ.get("camera_ip")
folder = os.environ.get("folder")

logger = utils.create_logger()

prev_preds = np.array([[]]).astype(np.float32)
reporter = IdleReporter(folder, server_url, configs["wait_time"], logger)
image_extractor = ImageHTTPExtractor(camera_ip, logger, username=username, password=password)
model_predictor = ModelPredictionsReceiver(server_url, logger)
algo = IdleAlgorithm(logger, image_extractor, model_predictor, reporter)

async def main():
    await asyncio.gather(run_sio(server_url + ':3456'), algo.start())

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
except Exception as exc:
    print(exc)
finally:
    loop.close()
