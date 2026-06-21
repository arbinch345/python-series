# clear() = Removes all the elements from the dictionary
car = {
    'brand': 'Rolex',
    'Model': 'Rolex_RRR',
    'Year': 2001,
    'color': 'Mlue'
}

car.clear()
print(car)


# copy() = Returns a copy of the dictionary
car1 = {
    'brand': 'Rolex',
    'Model': 'Rolex_RRR',
    'Year': 2001,
    'color': 'Mlue'
}

print(car1)
cp = car1.copy()
print(cp)


# get() = Returns the value of the specified key
car2 = {
    'brand': 'Rolex',
    'Model': 'Rolex_RRR',
    'Year': 2001,
    'color': 'Mlue'
}

print(car2.get('brand'))


# items() = Returns a list containing a tuple for each key value pair
car3 = {
    'brand': 'Rolex',
    'Model': 'Rolex_RRR',
    'Year': 2001,
    'color': 'Mlue'
}

for x, y in car3.items():
    print(f"{x}: {y}")


# keys() = Returns a list of containing the dicitionary's keys
car4 = {
    'brand': 'Rolex',
    'Model': 'Rolex_RRR',
    'Year': 2001,
    'color': 'Mlue'
}

# print(car4.keys())
for a in car4.keys():
    print(a)

# values() = Returns a list of all the values in the dictionary
car5 = {
    'brand': 'Rolex',
    'Model': 'Rolex_RRR',
    'Year': 2001,
    'color': 'Mlue'
}

# print(car5.values())
for b in car5.values():
    print(b)


# update() = Updates the dictionary with the specified key-value pairs
car5 = {
    'brand': 'Rolex',
    'Model': 'Rolex_RRR',
    'Year': 2001,
    'color': 'Mlue'
}

car5.update({'color': 'White'})
print(car5)


# pop() = Removes the element with the specified key
car6 = {
    'brand': 'Rolex',
    'Model': 'Rolex_RRR',
    'Year': 2001,
    'color': 'Mlue'
}

car6.pop('color')
print(car6)


# popitem() = Removes the last inserted  key-value pair
car7 = {
    'brand': 'Rolex',
    'Model': 'Rolex_RRR',
    'Year': 2001,
    'color': 'Mlue'
}

car7.popitem()
print(car7)


# fromkeys() = Returns a dictionary with the specifed keys and value
x = {'key1', 'key2', 'key3'}
y = 0

the_dict = dict.fromkeys(x, y)
print(the_dict)

x = {'key1', 'key2', 'key3'}
this_dict = dict.fromkeys(x)

print(this_dict)


# setdefault() = Returns the value of the specified key. 
            # If key does nto exist: insert the key, with the specified value
car8 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

i = car8.setdefault('model', 'Lambo')
print(i)


# del = removes the item with specified key name:
car9 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

del car9['brand']
print(car9)