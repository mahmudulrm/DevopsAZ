print("20 days are " + str(20) + " minutes")
print(f"20 days are {20 * 24 * 60} minutes")

#Veriables
calculattion_to_minutes = 24 * 60
name_of_unit = "minutes"

print(f"20 days are {20 * calculattion_to_minutes} {name_of_unit}")
print(f"25 days are {25 * calculattion_to_minutes} {name_of_unit}")
print(f"30 days are {30 * calculattion_to_minutes} {name_of_unit}")

#Function
def days_to_units(number_of_days):
    print(f"{number_of_days} days are {number_of_days * calculattion_to_minutes} {name_of_unit}")
    print("Function is working")


days_to_units(30)
days_to_units(100)