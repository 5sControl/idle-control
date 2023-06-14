import json


with open("confs/configs.json", "r") as conf:
    configs = json.load(conf)
    CONF_THRES = configs.get("conf_thres")
    IOU_THRES = configs.get("iou_thres")
    MODEL_PATH = configs.get("model_path")
    CLASSES = configs.get("classes")
    WAIT_TIME = configs.get("wait_time")
    THRESHOLD = configs.get("threshold")
