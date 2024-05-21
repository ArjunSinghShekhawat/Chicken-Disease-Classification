from src.logger import logging
from src.exception import CustomeException
import sys

try:
    a = 1/0
except Exception as e:
    logging.info("Error aai")
    raise CustomeException(e,sys)