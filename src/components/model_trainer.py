import os
import sys
from catboost import CatBoostRegressor
from sklearn.ensemble import(
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from dataclasses import dataclass
from src.utils import load_yaml
from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path:str = os.path.join('artifact','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info('****************************************Model Trainer Phase Started****************************************')
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1])
            
            models = {
                "RandomForest": RandomForestRegressor(),
                "DecisionTree": DecisionTreeRegressor(),
                "GradientBoosting": GradientBoostingRegressor(),
                "LinearRegression": LinearRegression(),
                "KNN": KNeighborsRegressor(),
                "XGB": XGBRegressor(),
                "CatBoosting": CatBoostRegressor(verbose=False)}
            
            logging.info('Evaluating the models')
            params = load_yaml(file_path=r'configs/params.yaml')
            model_report:dict = evaluate_models(X_train,y_train,X_test,y_test,models,params)

            logging.info('Get the best model score from dict')
            best_model_score = max(sorted(model_report.values()))

            # To get best model name from dict
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            save_object(file_path=self.model_trainer_config.trained_model_file_path,obj=best_model)

            predicted=best_model.predict(X_test)
            r2_square = r2_score(y_test, predicted)
            
            logging.info(f"Best Model: {best_model_name}, R2 Score: {r2_square}")
            logging.info('****************************************Model Trainer Phase Completed****************************************')

            return r2_square            

        except Exception as e:
            raise CustomException(e,sys)