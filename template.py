import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

file_list = [
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/pipeline/__init__.py",
    f"src/config/__init__.py",
    f"src/config/configuration.py",
    f"src/entity/__init__.py",
    f"src/constants/__init__.py",
    f"src/utils/__init__.py",
    f"src/exception.py",
    f"src/logger.py",
    f"params.yaml",
    f"requirements.txt",
    f"main.py",
    f"setup.py",
    f"README.md",
    f".gitignore",
    f"templates/index.html",
    f"templates/home.html"
]

for file_path in file_list:
    file_path = Path(file_path)
    filedir,filename = os.path.split(file_path)


    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info("Directory Successfully Created !")
    
    if (not os.path.exists(filename)) or (os.path.getsize(filename)==0):
        with open(filename,'w') as file_obj:
            pass
        logging.info("File Successfully Create !")
    else:
        logging.info(f"{filename} is already exists !")