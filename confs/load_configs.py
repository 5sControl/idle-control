import json


with open("confs/configs.json", "r") as conf:
    configs = json.load(conf)
    CONF_THRES_1 = configs.get("conf_thres_1")
    CONF_THRES_2 = configs.get("conf_thres_2")
    IOU_THRES = configs.get("iou_thres")
    FIRST_MODEL_PATH = configs.get("first_model_path")
    SECOND_MODEL_PATH = configs.get("second_model_path")
    CLASSES = configs.get("classes")
    WAIT_TIME = configs.get("wait_time")
    THRESHOLD = configs.get("threshold")
