from src.Text_Summarize.config.configuration import ConfigurationManager
from src.Text_Summarize.components.training_model import TrainingModel
from src.Text_Summarize import logger


STAGE_NAME = "Training Model Stage"


class TrainingModelPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        training_model_config = config.get_training_model_config()
        training_model_config = TrainingModel(config=training_model_config)
        training_model_config.train()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = TrainingModelPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise e
