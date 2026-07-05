from src.Text_Summarizer.config.configuration import ConfigurationManager
from src.Text_Summarizer.components.model_trainer import ModelTrainer
from src.Text_Summarizer.logger import logger

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        config_manager = ConfigurationManager()
        model_trainer_config = config_manager.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()