# Methods used in list

# append() = Adds an element at the end of the list
list1 = ['apple', 'orange', 'grapes']
list1.append('berry')

print(list1)


# clear() = removes all the element from the list
list2 = ['apple', 'orange', 'grapes']

list2.clear()
print(list2)


# copy() = Returns a copy of the list
list3 = ['apple', 'orange', 'grapes']

list3.copy()
print(list3)


# count() = Returns the number of elements with the specified value
list4 = ['apple', 'orange', 'grapes', 'apple', 'berry', 'apple']

result = list4.count('apple')                         # you have to introduce the variable
print(result)


# extend() = add the elements of a list, to the end of the current list
list5 = ['apple', 'orange', 'grapes']
a = ['berry', 'cherry', 'raspberry']

list5.extend(a)
print(list5)


# index() = returns the index of the first element with specified value
list6 = ['apple', 'orange', 'grapes', 'apple', 'berry', 'apple']

f = list6.index('berry')
print(f)


# insert() = adds an element at the specified position
list7 = ['apple', 'orange', 'grapes', 'berry']

list7.insert(0, 'watermelon')
print(list7)


# pop() = removes the element at the specified position
list8 = ['apple', 'orange', 'grapes', 'berry']

list8.pop(2)
print(list8)


# remove() = removes the item with the specified value
list9 = ['apple', 'orange', 'grapes', 'berry']

list9.remove('apple')
print(list9)


# reverse() = reverses the order of the list
list11 = ['apple', 'orange', 'grapes', 'berry']

list11.reverse()
print(list11)


# sort() = sorting (a-z) the list
list22 = ['apple', 'orange', 'grapes', 'berry']

list22.sort()
print(list22)


# joining the list using "+" operator
list_a = ['apple', 'orange', 'grapes', 'berry']
list_b = [1, 2, 3, 4, 5]

print(list_a + list_b)

# slice operator = copy of list using the ':' slice operator
thislist = ["apple", "banana", "cherry"]

mylist = thislist[:]
print(mylist)


thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)