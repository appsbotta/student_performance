import os
import yaml
import sys
from src.logger import logging
from src.exception import CustomException
from box import ConfigBox

def read_yaml(path_to_yaml:str) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            config = yaml.safe_load(yaml_file)
            logging.info('Read the config.yaml file')
            return ConfigBox(config)
    except Exception as e:
        raise CustomException(e,sys)