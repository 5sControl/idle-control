import time
from functional import *

def run():
    h = None
    while h is None:
        h = init_connection()
        time.sleep(1)

    model = init_model()

    while True:
        time.sleep(1)
        img0 = get_frame(h)
        if img0 is None: 
            continue
    
        boxes, scores, categories = predict(model, img0)
        img0 = put_rectangle(img0, boxes, scores)

        if len(categories):
            send_report_and_save_photo(img0)

            
if __name__ == '__main__':
    run()
