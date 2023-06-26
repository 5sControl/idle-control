import time
from functional import *


logger = create_logger()


def run():
    while (h := init_connection()) is None:
        logger.warning("Cannot create connection")
        time.sleep(1)
    model = init_model()
    logger.info("Model initialized")
    prev_preds = None
    iter_idx = 0
    while True:
        iter_idx += 1
        if iter_idx % 60 == 0:
            logger.info("60 iterations was passed")
        img, start_tracking = get_frame(h)
        if img is None:
            logger.warning("Empty photo")
            time.sleep(1)
            continue
        time.sleep(2)
        preds, scores = model(img)
        img = put_rectangle(img, preds.numpy(), scores.numpy())
        if len(scores) > 0:
            logger.info("Telephone was detected")
            if check_coordinates_diffs(prev_preds, preds):
                send_report_and_save_photo(img, start_tracking)
            prev_preds = preds


run()
