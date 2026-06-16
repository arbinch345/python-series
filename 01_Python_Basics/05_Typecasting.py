# Typecasting = It is the process of converting a variable from one data type to another.

name = "Tom"
age = 22
gpa = 3.2
is_student = True

# show the data type
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# integer into float data type
# age = float(age)
# print(age)
# print(type(age))

# float into integer data type
gpa = int(gpa)
print(gpa)
print(type(gpa))

# integer into string data type
age = str(age)
print(age)
print(type(age))

# string concat in python
age = str(age)
age += "1"         # it will show error if the value is not in string. only string and string will concat.
print(age)

# string to boolean data type
name = bool(name)
print(name)           # shows true value until the string is not empty, otherwise provide error.
print(type(name))

# shows false value because string is empty
name = ""
name = bool(name)
print(name)
print(type(name))

# float into string data type
gpa = 3.3
gpa = str(gpa)
print(gpa)
print(type(gpa))

# string can't be converted into "integer" or "float"
# name = "john"
# name = float(name)
# print(name)
# print(type(name))
# prints an error

# boolean to string
is_sale = False
is_sale = str(is_sale)
print(is_sale)
print(type(is_sale))

# possible typecasting
# float -------> integer
# integer -----> float
# string ------> boolean
# float -------> string
# integer -----> string
