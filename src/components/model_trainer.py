import os
import sys
from dataclasses import dataclass

from sklearn.metrics import roc_auc_score

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models
from src.components.models import get_models 

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1],
            )

            # Get the models from models.py
            models = get_models()

            # Evaluate models
            model_report: dict = evaluate_models(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models)

            # Extract the test scores from the report for sorting
            test_scores = {model_name: report['test_score'] for model_name, report in model_report.items()}

            # Get the best model score and name
            best_model_name = max(test_scores, key=test_scores.get)
            best_model_score = test_scores[best_model_name]
            best_model = models[best_model_name]
            
            logging.info(f"Model report: {model_report}")

            logging.info(f"Best found model: {best_model_name} with score {best_model_score}")
            
    
            

            # Save the best model
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            # Evaluate the best model
            predicted = best_model.predict_proba(X_test)[:, 1]
            auc_score = roc_auc_score(y_test, predicted)

            return auc_score

        except Exception as e:
            raise CustomException(str(e), e)


