#Dictionary Data Type

#list and for Loops
minutes = 24 * 60
hours = 24
name_of_unit = "minutes"

def days_to_units(number_of_days):
    units = days_and_unit_dictionary['unit']
    if units == "hours":
        return f"{number_of_days} days are {number_of_days * hours} {units}"
    elif units == "minutes":
        return f"{number_of_days} days are {number_of_days * minutes} {units}"
    else:
        return "Unsupported information"

def validation_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary['days'])
        if user_input_number > 0:
            calculation_value = days_to_units(user_input_number)
            print(calculation_value)
        elif user_input_number == 0:   
            print("you enter a Zero value, so no conversion for you!")
        else:
            print("Your inpurt is not valid number. Don't ruin my program")
    except ValueError:
        print("Your inpurt is not valid number. Don't ruin my program")

# Never exit
#while True:
#    user_input = input("Hay user, enter a number of days and I will convert it to minutus \n")
#    validation_and_execute()

#  exit 
user_input = ""
while user_input != "exit":
    user_input = input("Hay user, enter a number of days and unit \n")
    if user_input != "exit":
        days_and_unit = user_input.split(":")
        print(days_and_unit)
        days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
        print(days_and_unit_dictionary)
        validation_and_execute()