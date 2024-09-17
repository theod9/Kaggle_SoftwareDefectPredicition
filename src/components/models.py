from catboost import CatBoostClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import FunctionTransformer, StandardScaler
from sklearn.kernel_approximation import Nystroem
from sklearn.pipeline import make_pipeline
import numpy as np
from src.exception import CustomException  # Ensure you import CustomException for error handling

# Model-specific parameters
model_params = {
    "Hist Gradient Boosting": {
        'learning_rate': 0.05,
        'max_leaf_nodes': 33,
        'l2_regularization': 0.8,
        'min_samples_leaf': 300
    },
    "CatBoost": {
        'loss_function': 'Logloss',
        'eval_metric': 'AUC',
        'verbose': False
    },
    "Random Forest": {
        'n_estimators': 178,
        'max_depth': 10,
        'min_samples_split': 4,
        'min_samples_leaf': 10,
    },
    "XGBoost": {
        'n_estimators': 1696,
        'learning_rate': 0.01840,
        'max_depth': 3,
        'min_child_weight': 7,
        'subsample': 0.81301,
        'colsample_bytree': 0.97436,
        'gamma': 0.60546,
        'reg_alpha': 0.38077,
        'reg_lambda': 0.60503
    },
    "LightGBM": {
        'n_estimators': 1068,
        'learning_rate': 0.01649,
        'min_child_samples': 16,
        'subsample': 0.78621,
        'colsample_bytree': 0.52122,
        'min_split_gain': 0.77144,
        'reg_alpha': 0.77065,
        'reg_lambda': 0.35940,
        'num_leaves': 15,
        'cat_smooth': 19.77902,
        'verbose': -1
    },
}

def get_models():
    
    # Logistic Regression pipeline
    model_lr = make_pipeline(
        #FunctionTransformer(np.log1p),
        Nystroem(n_components=400, random_state=10),
        LogisticRegression(
            dual=False,
            C=0.024,
            class_weight='balanced',
            max_iter=1500,
            random_state=1,
            solver='newton-cholesky'
        )
    )

    models = {
        "Hist Gradient Boosting": HistGradientBoostingClassifier(**model_params["Hist Gradient Boosting"]),
        "CatBoost": CatBoostClassifier(**model_params["CatBoost"]),
        "Random Forest": RandomForestClassifier(**model_params["Random Forest"]),
        "Logistic Regression": model_lr,
        "XGBoost": XGBClassifier(**model_params["XGBoost"]),
        "LightGBM": LGBMClassifier(**model_params["LightGBM"]),
    }

    # Define the weights for the voting classifier
    voting_classifier_weights = {
        "Hist Gradient Boosting": 0.2,
        "CatBoost": 0.2,
        "Random Forest": 0.05,
        "Logistic Regression": 0.1,
        "XGBoost": 0.2,
        "LightGBM": 0.25,
    }

    try:
        # Check if the sum of the weights is equal to 1
        if not np.isclose(sum(voting_classifier_weights.values()), 1.0, rtol=1e-9):
            raise ValueError("The weights for the voting classifier must sum to 1.")
        
    except Exception as e:
        raise CustomException(str(e), e)

    # Add the Voting Classifier as one of the models
    voting_classifier = VotingClassifier(
        estimators=[(name, model) for name, model in models.items()],
        weights=[weight for weight in voting_classifier_weights.values()],
        voting='soft'
    )

    models["Voting Classifier"] = voting_classifier

    return models

