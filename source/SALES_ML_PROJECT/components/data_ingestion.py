import os
import sys
from source.SALES_ML_PROJECT.exception import CustomException
from source.SALES_ML_PROJECT.logger import logging
import pandas as pd
from source.SALES_ML_PROJECT.utils import read_sql_data
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifact','train.csv')
    test_data_path:str=os.path.join('artifact','test.csv')
    raw_data_path:str=os.path.join('artifact','raw.csv')
    

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        try:
            df=read_sql_data()
            logging.info("Reading from mysql database")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df, test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info('Data Ingestion completed')
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
            
            
            
        except Exception as e:
            raise CustomException(e,sys)
