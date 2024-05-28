
from src.Text_Summarize.config.configuration import ConfigurationManager
from src.Text_Summarize.components.evaluation_model import EvaluationModel




class EvaluationModelTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        evaluation_model_config = config.get_evaluation_model_config()
        evaluation_model_config = EvaluationModel(config=evaluation_model_config)
        evaluation_model_config.evaluate()