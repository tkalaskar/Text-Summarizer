from src.Text_Summarizer.config.configuration import ConfigurationManager
from src.Text_Summarizer.components.data_transformation import DataTransformation
from src.Text_Summarizer.logger import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config_manager = ConfigurationManager()
        data_transformation_config = config_manager.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()