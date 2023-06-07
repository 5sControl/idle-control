import time
from functional import *
import os

def run():
    while (h := init_connection()) is None:
        time.sleep(1)

    model = init_model()
    while True:
        time.sleep(2)
        if (img := get_frame(h)) is None: continue
        boxes, scores, categories = predict(model, img)
        img = put_rectangle(img, boxes, scores)

        if len(categories): send_report_and_save_photo(img)
            
if __name__ == '__main__':
    run()
