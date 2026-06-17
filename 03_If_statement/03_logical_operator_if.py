# and : Returns "True" if both statements are true
# or : Returns "True" if one of the statements is true
# not : Reverses the result, return "False" if the result is true


# and operator:
a = 200
b = 33
c = 500

if a > b and c > b:
    print("Both conditions are true")
else:
    print("Both Conditions are not true")



# or operator:
x = 200
y = 33
z = 500

if x > y or x > z:
    print("One of the condition is True")
else:
    print("Both conditions are True")



# not operator:
i = 33
j = 200

if not i > j:
    print("i is not greater than j")



# combining multiple operators:
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount applies!")



# User authentication check:
username = "Bro"
password = 'apple123'
is_verified = True

if username and password and is_verified:
    print("Login successful!")
else:
    print("Login Failed!")