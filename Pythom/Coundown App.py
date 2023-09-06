#Coundown App
import datetime

user_imput = input("Enter your goal with a deadline separated by colon\n")
input_list = user_imput.split(":")
goal = input_list[0]
deadline = input_list[1]
print(input_list)

print(datetime.datetime.strptime(deadline, "%d.%m.%Y"))

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")

today_date = datetime.datetime.today()

print(today_date)

print(deadline_date - today_date)