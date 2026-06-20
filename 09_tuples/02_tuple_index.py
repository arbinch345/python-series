# You can access the tuple items by referring to the index number, inside square brackets.

this_tuple = ('apple', 'banana', 'cherry', 'berry', 'grapes')

print(this_tuple[1])


# Range of Indexes:
tuple1 = ('apple', 'banana', 'cherry', 'berry', 'grapes', 'oranges')

print(tuple1[2:5])                  # 2nd index included 5th index excluded


tuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(tuple2[3:])
print(tuple2[:4])
print(tuple2[:])                            # prints whole item in the tuple


# Negative Indexing

tuple3 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(tuple3[-4:-2])               # -2nd position not included
print(tuple3[-5:])
print(tuple3[:-1])


# Start: End: Step
tuple4 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(tuple4[2:5:1])                # starts from 2nd position and skip 1 step
print(tuple4[-6:-1:2])
print(tuple4[::-1])                # reverse the item


# Reversing the item in tuple
tuple5 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

reversed_tuple = tuple5[::-1]
print(reversed_tuple)