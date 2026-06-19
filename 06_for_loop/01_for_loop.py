# for loop: used for iterating over a sequence
            # (that is either a list, a tuple, a dictionary, a set, or a string)


n = 0
for i in range(1, 11, n + 1):
    print(i)
    i += 1


# Looping through strings
fruits = ["apple", "cherry", "berry"]
for i in fruits:
    print(i)


# The break statement:
fruits1 = ["apple", "cherry", "berry"]
for x in fruits1:
    print(x)
    if x == "cherry":
        break


# continue statement:
fruits2 = ["apple", "cherry", "berry"]
for y in fruits2:
    if y == "apple":
        continue
    print(y)