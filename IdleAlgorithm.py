from logging import Logger
import asyncio
from connection import ImageHTTPExtractor, ModelPredictionsReceiver, IdleReporter
from confs import configs
import utils
import numpy as np


class IdleAlgorithm:
    def __init__(
            self, 
            logger: Logger, 
            image_extractor: ImageHTTPExtractor, 
            model_predictor: ModelPredictionsReceiver,
            reporter: IdleReporter
        ) -> None:
        self._logger = logger
        self._image_extractor = image_extractor
        self._model_predictor = model_predictor
        self._reporter = reporter

    async def run(self):
        iter_idx = 0
        while True:
            iter_idx += 1
            if iter_idx % 60 == 0:
                self._logger.info("60 iterations passed")
            img, start_tracking = self._image_extractor.get_snapshot()
            if img is None:
                asyncio.sleep(1)
                continue
            preds = self._model_predictor.predict(img)
            if preds is None:
                asyncio.sleep(1)
                continue
            if preds.size != 0 and not np.any(preds == 1.):
                self._logger.info("Telephone is detected")
                if utils.bboxes_not_equal(prev_preds, preds, configs["threshold"]):
                    utils.save_cropped_bbox(img, preds[:, :4])
                    img = utils.put_rectangle(img, preds[:, :4], preds[:, 4])
                    self._reporter.send_report(self._reporter.create_report(img, str(start_tracking)))
                else:
                    self._logger.debug("Equal bboxes")
                prev_preds = preds
            asyncio.sleep(2)