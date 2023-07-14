import time
from functional import *
from send_request import predict
from dotenv import load_dotenv
from IdleReporter import IdleReporter


password = os.environ.get("password")
if password is None:
    load_dotenv("confs/settings.env")
logger = create_logger()


def run():
    server_url = os.environ.get("server_url")
    while (h := init_connection()) is None:
        logger.warning("Cannot create connection")
        time.sleep(1)
    prev_preds = None
    iter_idx = 0
    folder = os.environ.get("folder")
    reporter = IdleReporter(folder, server_url)
    while True:
        iter_idx += 1
        if iter_idx % 60 == 0:
            logger.info("60 iterations passed")
        img, start_tracking = get_frame(h)
        start_tracking = str(start_tracking)
        if img is None:
            logger.warning("Empty photo")
            time.sleep(1)
            continue
        time.sleep(1)
        preds = predict(img, server_url, logger)
        if preds is None:
            logger.warning("Empty response")
            time.sleep(1)
            continue
        if len(preds) > 0:
            logger.info("Telephone is detected")
            if check_coordinates_diffs(prev_preds, preds):
                img = put_rectangle(img, preds[:, :4], preds[:, 4])
                reporter.send_report(reporter.create_report(img, start_tracking))
            prev_preds = preds


run()
