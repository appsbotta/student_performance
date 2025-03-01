import os
import yaml
import sys
from src.logger import logging
from src.exception import CustomException
from box import ConfigBox
import numpy as np
import pandas as pd
import dill
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

def read_yaml(path_to_yaml:str,FROM) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            config = yaml.safe_load(yaml_file)
            logging.info(f'Read the {path_to_yaml} file from {FROM}')
            return ConfigBox(config)
    except Exception as e:
        raise CustomException(e,sys)
    
def save_obj(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as f:
            dill.dump(obj,f)
    except Exception as e:
        raise CustomException(e,sys)

def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            # model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report
    except Exception as e:
        raise CustomException(e, sys)
    

def load_object(file_path:str):
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)