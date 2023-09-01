from logging import Logger
import asyncio
from connection import ImageHTTPExtractor, ModelPredictionsReceiver, IdleReporter
from confs import configs
import utils
import numpy as np
import time


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
        self._min_epoch_time = 2 # replace on config in future

    async def start(self) -> None:
        self.prev_preds = np.array([[]]).astype(np.float32)
        while True:
            start_epoch_time = time.time()
            self._run_one_idle_epoch()
            end_epoch_time = time.time()
            passed_time = end_epoch_time - start_epoch_time
            if passed_time < self._min_epoch_time:
                await asyncio.sleep(self._min_epoch_time - passed_time)

    def _run_one_idle_epoch(self) -> None:
            img, start_tracking = self._image_extractor.get_snapshot()
            if img is None:
                return
            preds = self._model_predictor.predict(img)
            if preds is None:
                return
            if preds.size != 0 and not np.any(preds == 1.):
                self._logger.info("Telephone is detected")
                if utils.bboxes_not_equal(self.prev_preds, preds, configs["threshold"]):
                    utils.save_cropped_bbox(img, preds[:, :4])
                    img = utils.put_rectangle(img, preds[:, :4], preds[:, 4])
                    self._reporter.send_report(self._reporter.create_report(img, str(start_tracking)))
                else:
                    self._logger.debug("Equal bboxes")
                self.prev_preds = preds
