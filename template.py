import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO)

project_name=""

file_list=[
    ".github/worrflow/.gitkeep",
    f"source/{project_name}/__init__.py",
    f"source/{project_name}/components/__init__.py",
    f"source/{project_name}/components/data_ingestion.py",
    f"source/{project_name}/components/data_transformation.py",
    f"source/{project_name}/components/model_trainer.py",
    f"source/{project_name}/components/model_monitering.py",
    f"source/{project_name}/pipelines/__init__.py",
    f"source/{project_name}/pipelines/training_pipeline.py",
    f"source/{project_name}/pipelines/prediction_pipeine.py",
    f"source/{project_name}/exception.py",
    f"source/{project_name}/logger.py",
    f"source/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"  
]




for filepath in file_list:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:{filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating empty file:{filepath}")
    
    
    else:
        logging.info(f"{filename} is already exists")
