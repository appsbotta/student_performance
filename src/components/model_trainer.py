import os
import sys
from dataclasses import dataclass

from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import *

config_path = 'config.yaml'
config = read_yaml(config_path,'model_trainer')

@dataclass
class ModelTrainerConfig:
    treained_model_file_path = os.path.join(config.model_trainer.root_dir,"model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self,train_arr,test_arr):
        try:
            logging.info("Split training and test input data")
            
            X_train,y_train,X_test,y_test = train_arr[:,:-1],train_arr[:,-1],test_arr[:,:-1],test_arr[:,-1]

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "K-NN" : KNeighborsRegressor(),
                "Xgboost": XGBRegressor(),
                "Ada Boost": AdaBoostRegressor(),
            }
            
            model_report:dict = evaluate_models(X_train,y_train,X_test,y_test,models)

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("no best model found",sys)
            logging.info(f"Best model is selected: {best_model_name}")

            save_obj(
                file_path=self.model_trainer_config.treained_model_file_path,
                obj = best_model
            )
            predicted=best_model.predict(X_test)
            r2_square = r2_score(y_test,predicted)
            return r2_square

        except Exception as e:
            raise CustomException(e,sys)