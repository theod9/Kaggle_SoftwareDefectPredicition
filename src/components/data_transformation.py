import os
import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('artifacts', "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
        self.numerical_columns = [
            'loc', 'v(g)', 'ev(g)', 'iv(g)', 'n', 'v', 'l', 'd', 'i', 'e', 'b', 't',
            'lOCode', 'lOComment', 'lOBlank', 'locCodeAndComment', 'uniq_Op',
            'uniq_Opnd', 'total_Op', 'total_Opnd', 'branchCount'
        ]

    def get_data_transformer_object(self):
        """
        This function creates the preprocessing pipeline for numerical columns.
        """
        try:
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            logging.info(f"Numerical columns: {self.numerical_columns}")

            # Only numerical columns are handled in the pipeline for now
            preprocessor = ColumnTransformer(
                transformers=[
                    ("num_pipeline", num_pipeline, self.numerical_columns)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(f"Error in get_data_transformer_object: {str(e)}", sys)

    def initiate_data_transformation(self, train_path: str, test_path: str):
        """
        Reads the train and test data, applies the preprocessing pipeline, and saves the preprocessor object.
        """
        try:
            # Ensure train and test data paths are valid
            if not os.path.exists(train_path) or not os.path.exists(test_path):
                raise FileNotFoundError(f"Train or Test file not found at the given paths: {train_path}, {test_path}")

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Successfully read train and test datasets.")

            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "defects"

            # Split the data into features and target
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying the preprocessing pipeline to training and testing data.")

            # Transform the data
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            # Combine features and target into one array
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Preprocessing completed and saved to: {self.data_transformation_config.preprocessor_obj_file_path}")

            # Save the preprocessing object
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return train_arr, test_arr, self.data_transformation_config.preprocessor_obj_file_path

        except FileNotFoundError as e:
            raise CustomException(f"FileNotFoundError: {str(e)}", e)
        except Exception as e:
            raise CustomException(f"Error in initiate_data_transformation: {str(e)}", e)
