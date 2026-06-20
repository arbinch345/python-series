# Loop through a list

# this_list = ['apple', 'orange', 'banana', 'cherry']

# for x in this_list:
#     print(x)                # print list one by one in new line


# Loop through index numbers
# my_list = ['apple', 'orange', 'banana', 'cherry']

# for i in range(len(my_list)):
#     print(my_list[i])


# Using a while loop
list_a = ['apple', 'orange', 'banana', 'cherry']
i = 0

while i < len(list_a):
    print(list_a[i])
    i = i + 1


# Looping Comprehension: the shortest syntax for looping through lists.
list_b = ["apple", "banana", "cherry"]

[print(x) for x in list_b]