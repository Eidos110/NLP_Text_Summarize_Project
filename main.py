from src.Text_Summarize import logger
from src.Text_Summarize.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.Text_Summarize.pipeline.stage_02_data_validation import DataValidationPipeline
from src.Text_Summarize.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.Text_Summarize.pipeline.stage_04_training_model import TrainingModelPipeline
from src.Text_Summarize.pipeline.stage_05_evaluation_model import EvaluationModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e
    


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Training Model Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    training_model = TrainingModelPipeline()
    training_model.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Evaluation Model Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    evaluation_model = EvaluationModelTrainingPipeline()
    evaluation_model.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e