from src.logging import logger
from src.pipeline.stage_1_data_ingestion import DataIngestionPipeline

STAGE_NAME = 'Data ingestion stage'

try:
    logger.info(f'Initiating {STAGE_NAME} intiated')
    Data_Ingestion_Pipeline = DataIngestionPipeline()
    Data_Ingestion_Pipeline.intiate_data_ingestion()
    logger.info(f'{STAGE_NAME} initiated')
except Exception as e:
    logger.exception(e)
    raise e