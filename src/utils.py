import os
import yaml
import sys
from src.logger import logging
from src.exception import CustomException
from box import ConfigBox
import numpy as np
import pandas as pd
import dill

def read_yaml(path_to_yaml:str) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            config = yaml.safe_load(yaml_file)
            logging.info('Read the config.yaml file')
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