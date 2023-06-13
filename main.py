import time
from functional import *
from dotenv import load_dotenv


def run():
    while (h := init_connection()) is None:
        time.sleep(1)
    model = init_model()
    prev_preds = None
    while True:
        time.sleep(5)
        if (img := get_frame(h)) is None:
            continue
        preds, scores = model(img)
        img = put_rectangle(img, preds.numpy(), scores.numpy())
        if len(scores) > 0:
            if check_coordinates_diffs(prev_preds, preds):
                send_report_and_save_photo(img)
            prev_preds = preds


load_dotenv("confs/settings.env")
run()
