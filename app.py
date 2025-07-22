from source.SALES_ML_PROJECT.logger import logging
from source.SALES_ML_PROJECT.exception import CustomException
import sys
from source.SALES_ML_PROJECT.components.data_ingestion import DataIngestion







if __name__=="__main__":
    logging.info("execution started")
    
    try:
        obj=DataIngestion()
        obj.initiate_data_ingestion()
        
        
    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e,sys)