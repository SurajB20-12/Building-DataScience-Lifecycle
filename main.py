from src.DataScience_lifecycle import logger
from src.DataScience_lifecycle.pipelines.data_validation_pipeline import (
    DataValidationTrainingPipeline,
)


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\n")
except Exception as e:
    logger.error(f"Error in stage {STAGE_NAME}: {e}")
    raise e
