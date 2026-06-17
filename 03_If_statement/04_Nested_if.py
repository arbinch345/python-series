# Nested if: Using of if statment inside if statement is nested if statments

age = int(input("Enter your age here: "))
has_license = True

if age >= 18:
    if has_license:
        print("You can drive!")
    else:
        print("You need a license!")
else:
    print("You are too young to drive!")



score = int(input("Enter your score here: "))
attendance = int(input("Enter your attendance here: "))
submitted = True

if score > 60:
    if attendance >= 80:
        if submitted:
            print("You've pass with good grade!")
        else:
            print("Pass but missing assignment!")
    else:
        print("Pass but low attendance!")
else:
    print("Fail!")



username = "Emily"
password = "Apple123"
is_active = True

if username:
    if password:
        if is_active:
            print("Login Successful!")
        else:
            print("Account is not active!")
    else:
        print("Password required!")
else:
    print("Username required!")