#1 import helper
#2 from helper import validation_and_execute, user_input_massages
from helper import *
#  exit 
user_input = ""
while user_input != "exit":
    user_input = input(user_input_massages)
    if user_input != "exit":
        days_and_unit = user_input.split(":")
        print(days_and_unit)
        days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
        print(days_and_unit_dictionary)
        #1 helper.validation_and_execute(days_and_unit_dictionary)
        validation_and_execute(days_and_unit_dictionary)