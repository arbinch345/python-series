# tuple = tuple items are ordered, unchangeable and allow duplicates. uses ().
        #   used to store multiple items in a single variable.


"""
ordered = the items have a defined order, and that order will not change.

Unchangeable = we cannot change, add or remove items after the tuple has been created.

Allow duplicates = since tuple are indexed, they can have items with the same value.
"""


# creating the tuple
this_tuple = ("apple", "banana", "cherry", "apple", "beryy")

print(this_tuple)


# tuple length
my_tuple = ("apple", "banana", "cherry", "apple", "beryy")

print(len(my_tuple))


# Create tuple in with one item with type() function
tuple1 = ("apple",)                     # remember the ',' comma

print(tuple1)
print(type(tuple1))


# Not a tuple
tuple2 = ("apple")

print(tuple2)
print(type(tuple2))


# Tuple - data types:
tuple_a = ('apple', 'banana', 'cherry')
tuple_b = (1, 2, 3, 4, 5)
tuple_c = (True, False)

# print(tuple_a, tuple_b, tuple_c)
print(tuple_a)
print(tuple_b)
print(tuple_c)


# combining together all the data types
tuple3 = ('abc', 1, True, 66, False, 'def')

print(tuple3)


# tuple() constructor:
tuple4 = tuple(("apple", "banana", "cherry"))         # use tuple() function with double round bracket

print(type(tuple4))
print(tuple4)