# Tuples are unchangeable, or immutable


# Add Items:
fruits = ('apple', 'banana', 'cherry')

x = list(fruits)
x[1] = "orange"
fruits = tuple(x)
print(fruits)


fruits1 = ('apple', 'banana', 'cherry')
x = list(fruits1)
x.append('orange')
fruits1 = tuple(x)

print(fruits1)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


# Remove Items:
fruits3 = ("apple", "banana", "cherry")
z = list(fruits3)
z.remove('banana')

fruits3 = tuple(z)
print(fruits3)


# Delete Tuple:
# fruits4 = ("apple", "banana", "cherry")
# del fruits4
# print(fruits4)                              # throws an error because tuple has already been deleted


# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple") 