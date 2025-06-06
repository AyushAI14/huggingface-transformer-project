from src.config.configuration import ConfigurationManager
from src.components.Data_trainer import ModelTrainer
from src.config.configuration import DataTrainerConfig 

class DataTrainerPipeline:
    def __init__(self):
        pass

    def intiate_data_trainer(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_data_trainer_config()
        model_trainer = ModelTrainer(config=DataTrainerConfig)
        model_trainer.train()



