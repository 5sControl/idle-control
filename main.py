import os
import time
from functional import *


os.environ['password'] = 'just4Taqtile'
os.environ['username'] = 'admin'
os.environ['camera_url'] = 'http://192.168.1.163/onvif-http/snapshot?Profile_1' 
os.environ['server_url'] = '192.168.1.999'
os.environ['folder'] = 'images/192.168.1.163'

def run():
    h = init_connection()
    model = init_model()

    while True:
        img0 = get_frame(h)
        if get_frame(h) is None:
            continue
    
        boxes, scores, categories = predict(model, img0)
        img0 = put_rectangle(img0, boxes, scores)

        if len(categories):
            send_report_and_save_photo(img0)

        time.sleep(1)
            
if __name__ == '__main__':
    run()
