from setuptools import find_packages, setup
from typing import List

def requirements(file_path:str) -> List[str]:
    req=[]
    with open(file_path) as f:
        pkg=f.readlines()
        req=[i.replace('\n',"") for i in pkg]
        

    return req


setup(
    name='Market_mix_ML_Project',
    version='0.0.1',
    author='Aditya',
    author_email='adi.763192@gmail.com',
    packages=find_packages(),
    install_requires=requirements('requirements.txt')
    
)