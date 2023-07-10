from PIL import Image
from flask import Flask, jsonify, request
from configs.load_configs import *
from IdleObjectDetectionModel import IdleObjectDetectionModel
import numpy as np
import io


app = Flask(__name__)
model = IdleObjectDetectionModel(
    MODEL_PATH,
    CONF_THRES,
    IOU_THRES,
    CLASSES
)

convert_bytes2image = lambda bytes: np.array(Image.open(io.BytesIO(bytes)), dtype=np.uint8)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        image = convert_bytes2image(request.files["image"].read())
        coords = model(image)
        return jsonify(
            {
                "coordinates": coords.tolist()
            }
        )
