# Dictionaries = a collection which is ordered, changeable and do not allow duplicates.
#                used to store data values in key: value pairs


# Creating the dictionary
the_dict = {
    'name': 'Mark',
    'surname': 'Bernal',
    'DOB': "16th April"
}

print(the_dict)


my_dict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'Year': 1964
}

print(my_dict['brand'])


# len() & type() function:
dict1 = {
    'brand': 'Ford',
    'model': 'Mustang',
    'Year': 1964
}

print(len(dict1))
print(type(dict1))


# dict() function constructor:
dict2 = dict(name = 'John', age = 26, country = 'Norway')

print(dict2)


#  To add the item in the dictionary
car8 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car8['color'] = 'Black'
print(car8)