"""
If statement = If the condition is true, run the code block inside the if statement.
               If the condition is false, skip the code and go to next step.

               
Elif = The elif keyword allows you to check multiple expressions. Execute the code if
the block of code is True. If not, skip the code and go to the next step.


Else = The 'else' statement is executed when the 'if' or 'elif' condition is false.
"""

# Note: python supports the usual logical conditions from mathematics.


a = 55
b = 34

if a > b:
    print("a is greater than b!")
else:
    print("b is greater than a!")



# WAP to check if the cycle of life.
age = int(input("Enter your age: "))

if age >= 13:
    print("You are young!")
elif age >= 18:
    print("You are teenager!")
elif age >= 35:
    print("You are middle age!")
else:
    print("You are old!")


# WAP to check your grade.
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade A!")
elif score >= 80:
    print("Grade B!")
elif score >= 80:
    print("Grade C!")
else:
    print("Grade D!")