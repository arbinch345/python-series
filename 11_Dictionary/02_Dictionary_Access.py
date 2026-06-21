# You can access the items of a dictionary by referring to its key name, inside square brackets.

# get() = give you the same result.
this_dict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': '1964'
}

print(this_dict.get('model'))

# Adding the item in dictionary
this_dict['color'] = 'white'
print(this_dict)



# keys() = return a list of all the keys in the dictinary.
dict1 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': '1964'
}

print(dict1.keys())


# values() = return a list of all values in dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(car.values())


# items() = return each item in a dictionary, as tuples in a list
car1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# print(car1.items())
# print(car1.items('brand'))         return error, as items() does not takes argument

# you can update items 
x  = car1.items()
print(x)
car['year'] = 2020

print(x)


# check if key Exists:
the_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

if 'model' in the_dict:
    print('Yes!')
else:
    print("No!")

if 'color' not in the_dict:
    print('Yes!')
else:
    print("NO!")