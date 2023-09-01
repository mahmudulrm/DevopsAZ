print("20 days are " + str(20) + " minutes")
print(f"20 days are {20 * 24 * 60} minutes")

#Veriables
calculattion_to_minutes = 24 * 60
name_of_unit = "minutes"

print(f"20 days are {20 * calculattion_to_minutes} {name_of_unit}")
print(f"25 days are {25 * calculattion_to_minutes} {name_of_unit}")
print(f"30 days are {30 * calculattion_to_minutes} {name_of_unit}")

#Function
def days_to_units(number_of_days, custom_message):
    print(f"{number_of_days} days are {number_of_days * calculattion_to_minutes} {name_of_unit}")
    print(f"Function is working {custom_message} ")


days_to_units(30, "GOOD")
days_to_units(100, "Awesome")
days_to_units(30, "okay")

#Scope variable and function

def scope_check(number_of_days):
    my_var = "Fuction Variable"
    print(number_of_days)
    print(my_var)

scope_check(20)

#user input //string 

##user_input = input("Enter number of days \n")
##print(user_input)

# Fuction return

def return_check(number_of_days):
    return f"your input is {number_of_days}"

my_var_return = return_check(5)

print(my_var_return)

#casting data type

user_input = input("Enter number of days \n")
user_input_number = int(user_input)
print(user_input_number)