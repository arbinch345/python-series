# Data Types: It is a set when you assign a value to a variable

# string: series of characters. It includes letters, integers, numbers, symbols
#         enclosed in single or double quotes

first_name = "Bro"
food = "pizza"
email = "bro@fake.com"

print(f"Hello {first_name}.")
print(f"My favourite food is {food}.")
print(f"My email is {email}.")


# integer: is a whole number. It can either positive or negative. only contain numbers and cannot be in quote.

age = 22
quantity = 5
num_of_students = 30

print(f"My age is {age}.")
print(f"You're buying {quantity} item.")
print(f"There are {num_of_students} students in the class.")


# float: a decimal number. can be either positive or negative and must have decimal point.

price = 19.99
gpa = 3.2
distance = 10.5

print(f"The price of the item is ${print}.")
print(f"I got {gpa} gpa in exam.")
print(f"You ran {distance} km.")


# Boolean (bool): datatype that can be either "True" or "False"
#                 Mostly used in conditions.

is_student = True 
if is_student:
    print("He is a student!")
else:
    print("He is not a student!")

is_sale = False
if is_sale:
    print("The item is in sale!")
else:
    print("The item is not on sale!")
