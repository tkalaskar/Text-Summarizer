from src.Text_Summarizer.config.configuration import ConfigurationManager
from src.Text_Summarizer.components.data_ingestion import DataIngestion
from src.Text_Summarizer.logger import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.unzip_and_clean()        
        logger.info("Data Ingestion Completed")
