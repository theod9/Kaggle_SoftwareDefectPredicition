import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import roc_auc_score


from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(str(e), e)
    

def evaluate_models(X_train, y_train, X_test, y_test, models):
    
    try:
        report = {}
        for name, model in models.items():
        
            model.fit(X_train, y_train) 
            test_preds = model.predict_proba(X_test)[:, 1]
            test_score = roc_auc_score(y_test, test_preds)

            report[name] = {
                'test_score': test_score
            }
        return report
        
    except Exception as e:
        raise CustomException(str(e),e)
            
    
    
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(str(e), e)