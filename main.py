from src.Text_Summarizer.logger import logger
from src.Text_Summarizer.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.Text_Summarizer.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.Text_Summarizer.pipeline.model_trainer import ModelTrainerPipeline

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"Encountered an error while running {STAGE_NAME}: {e}")
    raise e

STAGE_NAME = "Data Transformation"

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"Encountered an error while running {STAGE_NAME}: {e}")
    raise e


STAGE_NAME = "Model Training"

try:
    logger.info(f"Starting {STAGE_NAME}")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.error(f"Encountered an error while running {STAGE_NAME}: {e}")
    raise e