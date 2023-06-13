import time
from functional import *
from dotenv import load_dotenv


def run():
    while (h := init_connection()) is None:
        time.sleep(1)

    model = init_model()
    while True:
        time.sleep(2)
        if (img := get_frame(h)) is None:
            continue
        boxes, scores = model(img)
        img = put_rectangle(img, boxes.numpy(), scores.numpy())

        print(scores)
        if len(scores) > 0:
            send_report_and_save_photo(img)


load_dotenv("confs/settings.env")
run()
