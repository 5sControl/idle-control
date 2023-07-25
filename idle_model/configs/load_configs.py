import json


with open("configs/confs.json", "r") as conf:
    configs = json.load(conf)
CONF_THRES = configs.get("conf_thres")
CONF_PATH = configs.get("conf_path")
IOU_THRES = configs.get("iou_thres")
MODEL_PATH = configs.get("model_path")
CLASSES = configs.get("classes")
PORT = configs.get("port")
