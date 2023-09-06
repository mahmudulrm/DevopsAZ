#Modules cteate a file call helper.py
#1 import helper
#3 import helper as h
#2 from helper import validation_and_execute, user_input_massages
#from helper import *

import os
import logging

print(os.name)

logger = logging.getLogger("MAIN")
logger.error("Error happened in the app")