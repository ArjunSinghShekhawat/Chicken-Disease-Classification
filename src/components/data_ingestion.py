import os
import urllib.request as request
import zipfile
from src.logger import logging
from src.exception import CustomeException
from src.utils.common import get_size
from src.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,header = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logging.info(f"{filename} download with following info {header}")
        else:
            logging.info(f"File already exists of size : {get_size(Path(self.config.local_data_file))} ")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir

        os.makedirs(unzip_path,exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
