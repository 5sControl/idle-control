from PIL import Image
from flask import Flask, jsonify, request
from configs.load_configs import *
from IdleObjectDetectionModel import IdleObjectDetectionModel
import numpy as np
import io
import colorlog
import logging


app = Flask(__name__)
model = IdleObjectDetectionModel(
    MODEL_PATH,
    CONF_PATH,
    CONF_THRES,
    IOU_THRES,
    CLASSES
)

logger = logging.getLogger('min_max_logger')
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'CRITICAL': 'bold_red,bg_white',
        }))
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logger.propagate = False

convert_bytes2image = lambda bytes: np.array(Image.open(io.BytesIO(bytes)), dtype=np.uint8)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        image = convert_bytes2image(request.files["image"].read())
        coords = model(image)
        logger.info(f"Request to predict - {len(coords)}")
        return jsonify(
            {
                "coordinates": coords.tolist()
            }
        )
