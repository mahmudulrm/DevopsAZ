#Coundown App
#import datetime
from datetime import datetime

user_imput = input("Enter your goal with a deadline separated by colon\n")
input_list = user_imput.split(":")
goal = input_list[0]
deadline = input_list[1]
print(input_list)

print(datetime.strptime(deadline, "%d.%m.%Y"))

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()

time_till = deadline_date - today_date


print(f"Dear user! Time remaing for your goal: {goal} is {time_till} days")