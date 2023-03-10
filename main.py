from src.exception import CustomException
from src.logger import logging
import sys
from src.components.data_ingestion import DataIngestion

if __name__=="__main__":
    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.error(e)
        raise CustomException(e,sys)