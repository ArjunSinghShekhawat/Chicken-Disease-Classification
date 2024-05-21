import logging
import os
from datetime import datetime

FILE_PATH = f'{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log'
log_filepath = os.path.join(os.getcwd(),"logs",FILE_PATH)
os.makedirs(log_filepath,exist_ok=True)

Log_File = os.path.join(log_filepath,FILE_PATH)


logging.basicConfig(filename=Log_File,level=logging.INFO,format="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]")
