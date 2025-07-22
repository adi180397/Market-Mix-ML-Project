import os
import sys
from source.SALES_ML_PROJECT.exception import CustomException
from source.SALES_ML_PROJECT.logger import logging
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
import pymysql

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    logging.info("Reading SQL database started")
    
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info('connection established')
        df=pd.read_sql_query('select * from sales_data',mydb)
        
        return df
        
        
    except Exception as e:
        raise CustomException(e,sys)
    
    