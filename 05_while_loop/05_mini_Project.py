# simple calculator
is_running = True

while is_running:
    num1 = int(input("Enter the number here: "))
    num2 = int(input("Enter the number here: "))

    choice = int(input("Choice (1-5): "))

    if choice == 1:
        add = num1 + num2
        print(f"Addition: {num1} + {num2} = {add}")

    if choice == 2:
        sub = num1 - num2
        print(f"Subtraction: {num1} - {num2} = {sub}")

    if choice == 3:
        mul = num1 * num2
        print(f"Multiplication: {num1} * {num2} = {mul}")

    if choice == 4:
        div = num1 / num2
        print(f"Division: {num1} / {num2} = {div}")

    if choice == 5:
        break

    else:
        print("Invalid choice!")



# Multiplication Table Generator
mul = int(input('Enter the number here: '))
i = 0

while i <= 10:
    print(f"{mul} x {i} = {mul * i}")
    i += 1



# PIN verification:
is_pin = True
chance = 3

while is_pin:
    correct_pin = "4004"
    pin = input("Enter 4 digit pin: ")

    # check if the pin contains 4 digits and is numeric:
    if len(pin) != 4 or not pin.isdigit():
        print("Enter 4 digit pin only!")
        continue

    if pin == correct_pin:
        print("Phone unlocked!")
        break

    else:
        print("Incorrect pin!")
        chance -= 1
        if chance == 0:
            break
        print(f"Your chance now: {chance}")