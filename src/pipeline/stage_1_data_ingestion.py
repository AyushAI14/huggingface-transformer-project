from src.config.configuration import ConfigurationManager
from src.components.Data_ingestion import DataIngestion

class DataIngestionPipeline:
    def __init__(self):
        pass

    def intiate_data_ingestion(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)

        data_ingestion.downlaod_file()
        data_ingestion.extract_zip_file()