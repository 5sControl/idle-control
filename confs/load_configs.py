import json
import os


def load_configs() -> dict:
    with open("confs/configs.json", "r") as conf:
        configs = json.load(conf)
    return configs
