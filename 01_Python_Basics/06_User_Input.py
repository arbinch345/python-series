# input() = It is a function that prompts user to enter data.
# Returns the entered data into string.

name = input("What is your name?: ")
age = int(input("How old are you?:  "))

age += 1

print(f"My name is {name}. ")
print("HAPPY BIRTHDAY!")
print(f"I am {age} years old.")


# Exercise1: Find the area of rectangle

length = float(input("Enter the length of Rectangle: "))
width = float(input("Enter the width of Rectangle: "))
area = length * width

print(f"The area of the rectangle is {area} cm2.")


# Exercise2: Shopping cart program

item = input("What would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like to buy?: "))

total_price = price * quantity

print(f"You bought {quantity} X {item}/s.")
print(f"You're total price is ${total_price}")