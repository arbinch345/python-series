# frozen set = immutable version of set, contains unique , unordered, unchangeable elements.

#               you cannot add, remove, or modify its elements once it is defined 


# creating a frozen set
x = frozenset({'apple', 'orange', 'mango'})

print(x)
print(type(x))


# copy() = returns a shallow copy
fruits1 = frozenset({'apple', 'orange', 'mango'})
cp = fruits1.copy()

print(fruits1)
print(cp)


# difference() = returns a new forzenset with the difference
num1 = frozenset({1, 2, 3, 4})
num2 = frozenset({3, 4, 5, 6})

num3 = num1.difference(num2)
print(num3)                                 # prints 1,2 because it takes difference of 1st set.
# print(num1 - num2)                        # provides the same output


# intersection() = returns a new forzenset with the intersection. (matching output in both set)
a = frozenset({1, 2, 3, 4, 5})
b = frozenset({4, 5, 6, 7, 8})

c = a.intersection(b)
print(c)
# print(a & b)


# isdijoint() = returns whether two frozensets have an intersection
num4 = frozenset({1, 2, 3, 4, 5})
num5 = frozenset({4, 5, 6, 7, 8})
num6 = frozenset({9, 10, 11, 12})

print(num4.isdisjoint(num5))                    # returns 'False', there is intersection
print(num5.isdisjoint(num6))                    # retuns 'True', there is no intersection


# issubset() = Returns True if frozenset is a (proper) superset of another.
num7 = frozenset({1, 2})
num8 = frozenset({1, 2, 4})
num9 = frozenset({7, 9, 8})

print(num7.issubset(num8))                      # Returns 'true', both num7 & num8 sets are initialize with num 1, 2.
print(num8.issubset(num9))                      # Returns 'false'

# You can print in this way too:
print(num7 <= num8)
print(num7 < num8)


# issuperset = Returns True if frozenset with the symmetric difference
num11 = ({1, 2, 3})
num12 = ({1, 2})

print(num11.issuperset(num12))


# symmetric_difference() = Returns a new forzenset with the symmetic differences (similar item will be removed)
num13 = ({1, 2, 3, 4})
num14 = ({3, 4, 5, 6})

print(num13.symmetric_difference(num14))


# union() = Returns new frozenset containing the union
num15 = ({1, 2, 3})
num16 = ({3, 4, 5})

print(num15.union(num16))