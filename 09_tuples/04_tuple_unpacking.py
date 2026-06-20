# Tuple_packing = when we create tuple, we normally assign value. This is called "packing".

# Tuple_Unpacking = Extracting value back into variables, is "packing".

fruits = ('apple', 'banana', 'cherry')

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# Using *
fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(blue, orange, *violet) = fruits1

print(blue)
print(orange)
print(*violet)


fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(mlue, *grey, black) = fruits2

print(mlue)
print(*grey)
print(black)