from src.config.configuration import ConfigurationManager
from src.components.Data_evalution import ModelEvaluation

class DataEvalutionPipeline:
    def __init__(self):
        pass

    def intiate_data_evalution(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_data_evalution_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()



