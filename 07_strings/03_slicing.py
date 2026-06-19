# you can return a range of characters by using the slice syntax.
# specify the start index and the end index, separated by a colon, to return a part of the string.

b = "Hello, World!"

print(b[2:5])
print(b[:5])
print(b[0:])


# Negative Indexing: Use negative indexes to start the slice from the end of the string:

b = "Hello, World!"

print(b[-1: -5])
print(b[-1:])
print(b[-13:])
print(b[:-1])