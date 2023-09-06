#lsit Value
my_set = {"day1", "day2", "day3"}
#print(my_list[2])

my_set.add("day4")


for my_list_element in set(my_set):
    print(my_list_element)


print(type(set(my_set)))

my_list = ["day1", "day2", "day3", "day1"]
my_list.remove("day1")
print(my_list)