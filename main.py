from src.datascience import logger 
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

logger.info("Welcome to our custom logging data science")

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>>>stage{STAGE_NAME} started <<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>stage{STAGE_NAME} completed <<<<<")
except Exception as e:
     logger.exception(e)
     raise e
