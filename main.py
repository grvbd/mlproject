from src.exception import CustomException
from src.logger import logging
import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__=="__main__":
    try:
        print('Training Pipeline Started')
        logging.info('Training Pipeline Started')
        data_ingestion = DataIngestion()
        train_data_path,test_data_path = data_ingestion.initiate_data_ingestion()
        data_transformation=DataTransformation()
        train_array,test_array,_ = data_transformation.initiate_data_transformation(train_data_path,test_data_path)
        model_trainer = ModelTrainer()
        model_trainer.initiate_model_trainer(train_array,test_array)
        logging.info('Training Pipeline Completed')
        print('Training Pipeline Completed')
        
    except Exception as e:
        logging.error(e)
        raise CustomException(e,sys)