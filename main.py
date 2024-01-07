from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline


STAGE_NAME = 'Data Ingestion Stage'

try:
        logger.info(f">>> Stage {STAGE_NAME} started <<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>> Stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"
try:
        logger.info(f">>> Stage {STAGE_NAME} started <<<")
        prepare_base_model_pipeline = PrepareBaseModelPipeline()
        prepare_base_model_pipeline.main()
        logger.info(f">>> Stage {STAGE_NAME} completed <<<")
except Exception as e:
        logger.exception(e)
        raise e