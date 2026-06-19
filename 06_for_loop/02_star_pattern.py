# Star pattern
rows = 5
for i in range(rows):
    for j in range(rows):
        print("*", end =" ")
    print()


rows = 5
for i in range(i + 1):
    for j in range(i + 1):
        print("*", end = " ")
    print()


# full triangle:
row = 5

# upper part
for i in range(row):
    for j in range(rows - i - 1):
        print(" ", end="")

    for k in range(2 * i + 1):
        print("*", end="")
    
    print()

# lower part
for i in range(row - 2, -1, -1):
    for j in range(row - i - 1):
        print(" ", end="")

    for k in range(2 * i + 1):
        print("*", end="")
    
    print()