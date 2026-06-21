# SET METHODS:

# add(): adds an element to the set
set1 = {'apple', 'banana', 'cherry'}
set1.add('orange')

print(set1)


# clear() = Removes all the elements from the set
set2 = {'apple', 'banana', 'cherry'}
set2.clear()

print(set2)


# copy() = Returns a copy of the set
set3 = {'apple', 'banana', 'cherry'}
cp = set3.copy()

print(set3)
print(cp)


# difference() = Returns a set containing the difference between two or more sets
num1 = {1, 2, 3, 4}
num2 = {3, 4, 5, 6}

print(num1.difference(num2))
# print(num1 - num2)


# difference update() = Removes the items in the set that are also included in another, specified set
x = {'apple', 'banana', 'cherry'}
y = {'apple', 'mango', 'berry'}

x.difference_update(y)
print(x)


# discard() = Remove the specified item
set4 = {'apple', 'banana', 'cherry'}
set4.discard('banana')

print(set4)


# intersection() = Returns a set, that is the intersection of two other set
a = {1, 2, 3}
b = {3, 4, 5}

print(a.intersection(b))


# intersection.update() = Removes the items in the set that are also included in another, specified set
i = {"apple", "banana", "cherry"}
j = {"google", "microsoft", "apple"}

i.difference_update(j)
print(i)


# isdisjoint() = Returns whether two sets have a intersection or not
set5 = {1, 2, 3}
set6 = {0, 4, 5}

print(set5.isdisjoint(set6))


# issubset() = Returns True if all items of the set is present in another set
set7 = {1, 2}
set8 = {1, 2, 3}

print(set7.issubset(set8))


# issuperset() = Returns true if all items of another set (setB) is present in (setA).
set_a = {1, 2, 3}
set_b = {1, 2}

print(set_a.issuperset(set_b))


# pop() = Removes an element from the set
set_c = {1, 2, 3, 4, 5}
set_c.pop()

print(set_c)


# remove() = removes the specified element
set_d = {'apple', 'cherry', 'berry'}

set_d.remove('berry')
print(set_d)


# symmetric_difference() = Returns a set with the symmertric differences of two sets.
num11 = {1, 2, 3}
num12 = {3, 4, 5}

print(num11.symmetric_difference(num12))


# symmetric-difference_update() = Inserts the symmetric differences from set_A and set_B
m = {1, 2, 3, 4}
n = {3, 4, 5, 6}
m.symmetric_difference_update(n)
print(m)


# union() = Return a set containing the union of sets
num22 = {1, 2, 3, 4}
num23 = {3, 4, 5, 6}

z = num22 | num23
print(z)
# print(num22.union(num23))


# update() = Update the set with the union of the set_A and set_B
fruits = {'apple', 'berry', 'cherry'}
flower = {'Rose', 'Marigold', 'sunflower'}
fruits.update(flower)

print(fruits)