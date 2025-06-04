from src.constants import *
from src.utils.common import read_yaml_file,createDirs
from src.entity import DataIngestionConfig 

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