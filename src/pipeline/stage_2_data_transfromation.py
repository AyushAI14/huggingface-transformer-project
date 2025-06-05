from src.config.configuration import ConfigurationManager
from src.components.Data_Transformation import DataTransformation 

class DataTransformationPipeline:
    def __init__(self):
        pass

    def intiate_data_transformation(self):
        config = ConfigurationManager()
        data_tranformation_config = config.get_data_transformation_config()
        datatransformation=DataTransformation(config=data_tranformation_config)
        datatransformation.convert()