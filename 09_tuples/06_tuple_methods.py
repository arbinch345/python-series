# count() = Returns the number of times a specified value occurs in a tuple

fruits = ('apple', 'banana', 'orange', 'apple', 'grapes', 'berry', 'orange', 'apple')

result = fruits.count('apple')
print(result)


# index() = Searches the tuple for a specified value and returns the position of where it was found
fruits = ('apple', 'banana', 'orange', 'apple', 'grapes', 'berry', 'orange', 'apple')

output = fruits.index('orange')
print(output)


# Join Tuples
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


# Multiply Tuples
my_tuple = ('apple', 'cherry', 'berry')

print(my_tuple * 2)


my_tuple1 = ('apple', 'cherry', 'berry')

a = list(my_tuple1)
a.append('orange')
my_tuple1 = tuple(a)
print(a)