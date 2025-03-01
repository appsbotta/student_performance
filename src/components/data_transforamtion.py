import sys
import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import logging
from src.utils import save_obj,read_yaml

config_path = 'config.yaml'
config = read_yaml(config_path)

params_path = 'params.yaml'
params = read_yaml(params_path)

@dataclass
class DataTransformationConfig:
    preprocessor_ob_file_path=os.path.join(config.data_transformation.root_dir,"preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_col = list(params.num_col)
            categorical_col = list(params.cat_col)

            num_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]
            )
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False)),
                ]
            )
            logging.info(f"Categorical col: {categorical_col}")
            logging.info(f"Numerical cols: {numerical_col}")
            
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_col),
                    ("cat_pipeline",cat_pipeline,categorical_col),
                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Reading of both train and test data is completed")

            logging.info("Obtaining Preprocessor Object")
            preprocessor_obj = self.get_data_transformer_object()

            target_col_name = params.target_col

            input_feature_train_df = train_df.drop(columns=[target_col_name],axis=1)
            target_feature_train_df = train_df[target_col_name]

            input_feature_test_df = test_df.drop(columns=[target_col_name],axis=1)
            target_feature_test_df = test_df[target_col_name]

            logging.info("Applying preprocessor object on the train and test df")

            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)

            train_arr  = np.c_[
                input_feature_train_arr,np.array(target_feature_train_df)
            ]
            test_arr = np.c_[
                input_feature_test_arr,np.array(target_feature_test_df)
            ]
            logging.info("Saved Preprocessing Object")
            
            save_obj(
                file_path = self.data_transformation_config.preprocessor_ob_file_path,
                obj = preprocessor_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_ob_file_path,
            )

        except Exception as e:
            raise CustomException(e,sys)
