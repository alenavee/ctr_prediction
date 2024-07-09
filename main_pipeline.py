import json
import logging
import sys
import argparse
from datetime import datetime

import pandas as pd

from src.data.make_dataset import read_data, split_train_val_data
from src.entities.train_pipeline_params import (
    TrainingPipelineParams,
    read_training_pipeline_params
)

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def train_pipline(config_path: str):
    training_pipeline_params: TrainingPipelineParams = read_training_pipeline_params(config_path)

    data: pd.DataFrame = read_data(training_pipeline_params.input_data_path)
    data["hour"] = data.hour.apply(lambda val: datetime.strptime(str(val), "%y%m%d%H"))
    logger.debug(f"Start train pipline with params {training_pipeline_params}")
    logger.debug(f"data: {data.shape} \n {data.info()} \n {data.nunique()}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/train_config.yaml")
    args = parser.parse_args()
    train_pipline(args.config)
