import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook/data/train_Kaggle.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(str(e),e)
        
        
    def get_feature_statistics(self):
        """
        This method calculates and returns the min, max, and median for each feature in the train dataset.
        """
        try:
            # Read the train dataset
            train_data_path = self.ingestion_config.train_data_path
            train_set = pd.read_csv(train_data_path)

            # Calculate min, max, and median for each feature in the train set
            stats = train_set.describe().T[['min', 'max']]
            # get the half range
            stats['midrange'] = (stats['max'] - stats['min'])/2
            stats['median'] = train_set.median()

            return stats
        except Exception as e:
            raise CustomException(f"Error calculating feature statistics: {str(e)}", e)
        
# if __name__=="__main__":
    

#     obj=DataIngestion()
#     train_data,test_data = obj.initiate_data_ingestion()
        

#     data_transformation=DataTransformation()
#     train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

#     modeltrainer=ModelTrainer()
#     print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
    

