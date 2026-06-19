# multiplication table:
num = int(input("Enter a number here: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# countdown Timer:
for i in range(10, 0, -1):
    print(i)

print("Time up!")


# Factorial calculator:
num1 = int(input("Enter a number here: "))
fact = 1

for i in range(1, num1 + 1):
    fact *= i

print(f"Factorial: {fact}")