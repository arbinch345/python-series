# sets = set is a collection which is unordered, unchangeable, and unindexed.
#        used to store multiple items in a single variable. 
#        used "{}" brackets.

"""
Unordered = items doesn't have any defined order. and cannot be referred by index or key.

Unchangeable = we cannot change the items after the set has been create.

Allow Duplicates = sets cannot have two items with the same value.
"""

the_set = {"apple", "cola", "banana", "cherry", "mango"}

print(the_set)


# Duplicates Not Allowed
set1 = {"apple", "cola", "apple", "banana", "cherry", "mango"}

print(set1)


# 'True' and '1' is considered as same value
set2 = {"apple", "cola", "banana", "cherry", "mango", True, 1, 2}

print(set2)                 # True as output and ignores 1


set3 = {"apple", "cola", "banana", "cherry", "mango", False, 0}

print(set3)


# Sets - Data types
set4 = {'apple', 'cherry', 'mango'}
set5 = {3 ,5, 7, 9}
set6 = {True, False}

# print(set4, set5, set6)
print(set4)
print(set5)
print(set6)


# Data Types together
set7 = {'abc', True, 13, 'bro'}

print(set7)


# type of set
set_a ={"apple", "cola", "banana", "cherry", "mango", True, 1, 2}

print(type(set_a))
print(len(set_a))


# set constructor
this_set = set(('apple', 'cherry', 'mango'))

print(this_set)