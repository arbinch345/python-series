# indexing = accessing the particular position by referring the index number.

the_list = ["apple", "banana", "cherry", "orange", "watermelon"]

print(the_list[0])
print(the_list[: 3])          # exclude the 3rd position
print(the_list[2: ])          # print from 2nd and all 


# negative Indexing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[-4: -1])
print(thislist[ : -1])                   # exclude the last position -1
print(thislist[-5:])


# Start: End: Step
my_list =  ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(my_list[1:6:2])           # Jumps with 2 step
print(my_list[::-1])            # reverse the list


# check if item exists
list = ["apple", "banana", "cherry"]

if "apple" in list:
    print("YES!")
else:
    print("NOT!")

if "apple" not in list:
    print("YES")
else:
    print("NOT!")