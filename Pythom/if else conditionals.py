#if else conditionals
calculattion_to_minutes = 24 * 60
name_of_unit = "minutes"

def days_to_units(number_of_days):
 #Check condition 
    print(number_of_days > 0)
    condition_check = number_of_days > 0
 #Check data Type     
    print(type(condition_check))
    if number_of_days > 0:
        return f"{number_of_days} days are {number_of_days * calculattion_to_minutes} {name_of_unit}"
    elif number_of_days == 0:
         return "you enter a Zero value, so no conversion for you!"
    else:
        print(number_of_days > 0)
        return "you enter a negative value, so no conversion for you!"


user_input = input("Enter number of days \n")
user_input_number = int(user_input)

calculation_value = days_to_units(user_input_number)
print(calculation_value)


 #Check data Type string, int, float:
print(type("string check"))
print(type(30))
print(type(30.51))