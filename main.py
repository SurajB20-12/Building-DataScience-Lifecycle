from src.DataScience_lifecycle import logger
from src.DataScience_lifecycle.pipelines.data_ingestion_pipeline import (
    DataIngestionTrainingPipeline,
)

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\n")
except Exception as e:
    logger.error(f"Error in stage {STAGE_NAME}: {e}")
    raise e
