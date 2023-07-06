from PIL import Image
from flask import Flask, jsonify, request
from configs.load_configs import *
from IdleObjectDetectionModel import IdleObjectDetectionModel
import numpy as np


app = Flask(__name__)
model = IdleObjectDetectionModel(
    MODEL_PATH,
    CONF_THRES,
    IOU_THRES,
    CLASSES
)


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        image = np.array(request.json['image']).astype(np.float32)
        coords, confs = model(image)
        return jsonify(
            {
                "coordinates": coords.tolist(),
                "confidences": confs.tolist()
            }
        )
