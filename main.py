from src.logging import logger
from src.pipeline.stage_1_data_ingestion import DataIngestionPipeline
from src.pipeline.stage_2_data_transfromation import DataTransformationPipeline
from src.pipeline.stage_3_data_trainer import DataTrainerPipeline


STAGE_NAME = 'Data ingestion stage'

try:
    logger.info(f'Initiating {STAGE_NAME} intiated')
    Data_Ingestion_Pipeline = DataIngestionPipeline()
    Data_Ingestion_Pipeline.intiate_data_ingestion()
    logger.info(f'{STAGE_NAME} initiated')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Transformation stage'

try:
    logger.info(f'Initiating {STAGE_NAME} intiated')
    Data_transformation_Pipeline = DataTransformationPipeline()
    Data_transformation_Pipeline.intiate_data_transformation()
    logger.info(f'{STAGE_NAME} initiated')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Trainer stage'

try:
    logger.info(f'Initiating {STAGE_NAME} intiated')
    Data_trainer_Pipeline = DataTrainerPipeline()
    Data_trainer_Pipeline.intiate_data_trainer()
    logger.info(f'{STAGE_NAME} initiated')
except Exception as e:
    logger.exception(e)
    raise e


