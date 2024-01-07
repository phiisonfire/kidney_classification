from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_training import Training
from cnnClassifier import logger

STAGE_NAME = "Training"
class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__ == '__main__':
    try:
        logger.info(f">>> Stage {STAGE_NAME} started <<<")
        model_training_pipeline = ModelTrainingPipeline()
        model_training_pipeline.main()
        logger.info(f">>> Stage {STAGE_NAME} completed <<<")
    except Exception as e:
        logger.exception(e)
        raise e


