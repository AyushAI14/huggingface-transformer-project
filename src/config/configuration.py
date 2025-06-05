from src.constants import *
from src.utils.common import read_yaml_file,createDirs
from src.entity import DataIngestionConfig ,DataTransformationConfig

class ConfigurationManager:
    def __init__(self,
                 config_path=CONFIG_FILE_PATH,
                 param_path=PARAMS_FILE_PATH):
        self.config = read_yaml_file(config_path)
        self.params = read_yaml_file(param_path)
        createDirs([self.config.artifacts_root])


    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config.data_ingestion
        createDirs([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config 

    def get_data_transformation_config(self)-> DataTransformationConfig:
        config=self.config.data_transformation 
        createDirs([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path),
            tokenizer_name=str(config.tokenizer_name),
            train_path=Path(config.train_path),
            val_path=Path(config.val_path),
            test_path=Path(config.test_path)
        )
        return data_transformation_config 