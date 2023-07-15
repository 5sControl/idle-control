import json


with open("confs/configs.json", "r") as conf:
    configs = json.load(conf)
WAIT_TIME = configs.get("wait_time")
THRESHOLD = configs.get("threshold")
