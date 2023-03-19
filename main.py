from src.exception import CustomException
from src.logger import logging
import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.pipeline.training_pipeline import TrainPipeline

if __name__=="__main__":
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.start_train_pipeline()
        
    except Exception as e:
        logging.error(e)
        raise CustomException(e,sys)