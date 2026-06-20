"""
List = lists are used to store multiple items in a single variable.

List are one of 4 built-in data types in python to store collections of data, 
the other 3 are Tuple, set, and Dictionary.
"""

# List items are ordered, changeable, and allow duplicate values.

"""
Ordered = when we say that lists are ordered, it means that the items have a defined
          order, and that order will not change.
          If you add new items to a list, the new items will be placed at the end of the list.


Changeable = The list is changeable, that means we can change, add, and remove items in a list
            after it has been created.


Allow duplicate = since lists are indexed, lists can have items with the same value.
"""

# creating the list
the_list = ["apple", "banana", "orange"]            # creating the list

print(the_list)


# allow duplicates
the_list = ["apple", "banana", "orange", "apple", "cherry"]             # alllow duplicates

print(the_list)


# length of list
my_list = ["apple", "orange", "cherry"]

print(len(my_list))


# Data_types in list
list1 = ["apple", "orange", "cherry"]
list2 = [1,2,3,44,56,324]
list3 = [True, False]

print(list1)
print(list2)
print(list3)

# can take all data types at once
my_list = ["orange", 34, True, "male"]

print(my_list)
print(type(my_list))


# constructor = creates list using list() function.
my_list = list(("apple", "orange"))

print(my_list)
print(type(my_list))