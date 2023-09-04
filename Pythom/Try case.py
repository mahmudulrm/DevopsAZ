#Try case
calculattion_to_minutes = 24 * 60
name_of_unit = "minutes"

def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculattion_to_minutes} {name_of_unit}"


user_input = input("Enter number of days \n")
try:
    user_input_number = int(user_input)
    if user_input_number > 0:
        calculation_value = days_to_units(user_input_number)
        print(calculation_value)
    elif user_input_number == 0:   
        print("you enter a Zero value, so no conversion for you!")
except ValueError:
    print("Your inpurt is not valid number. Don't ruin my program")

