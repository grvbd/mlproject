from src.exception import CustomException
from src.logger import logging
import sys

if __name__=="__main__":
    try:
        logging.info('Started the program')
        x = 4/0
        logging.info('Ended the program')
    except Exception as e:
        logging.error(e)
        raise CustomException(e,sys)