#list and for Loops
calculattion_to_minutes = 24 * 60
name_of_unit = "minutes"

def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculattion_to_minutes} {name_of_unit}"

def validation_and_execute():
    try:
        user_input_number = int(number_of_days_element)
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
    user_input = input("Hay user, enter a number of days and I will convert it to minutus \n")
    print(type(user_input.split(",")))
    print(user_input.split(","))
    if user_input != "exit":
      for number_of_days_element in user_input.split(","):
        validation_and_execute()