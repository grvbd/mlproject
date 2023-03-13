import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifact','train.csv')
    test_data_path:str = os.path.join('artifact','test.csv')
    raw_data_path:str = os.path.join('artifact','data.csv')

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info(f'****************************************Data Ingestion Phase Started****************************************')
            
            logging.info('Reading the raw dataset as dataframe')
            df = pd.read_csv('D:\DS\Workouts\Krish Naik\DS_IS\mlproject\data\stud.csv')
            
            dir_path = os.path.dirname(self.data_ingestion_config.raw_data_path)
            
            os.makedirs(dir_path, exist_ok=True)
            df.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)
            logging.info('Saved raw data')
            
            logging.info('Train test split initiated')
            train_df,test_df = train_test_split(df,test_size=0.2,random_state=42)
            
            dir_path = os.path.dirname(self.data_ingestion_config.train_data_path)
            os.makedirs(dir_path, exist_ok=True)
            train_df.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            logging.info('Saved train data')

            dir_path = os.path.dirname(self.data_ingestion_config.test_data_path)
            os.makedirs(dir_path, exist_ok=True)
            test_df.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)
            logging.info('Saved test data')
            logging.info(f"Train data path: {self.data_ingestion_config.train_data_path}, Test data path: {self.data_ingestion_config.test_data_path}")
            logging.info('****************************************Data Ingestion Phase Completed****************************************')
            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path)
        
        except Exception as e:
            raise CustomException(e,sys)
    