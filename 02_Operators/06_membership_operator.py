# Membership operator are use to test if a sequence is presented in the object.


# in = Returns True if a sequence with the specified value is present in the object.
x = "1, 2, 3, 4, 5, 7"

print('2' in x)                    # returns 'TRUE', the item is present in the defined variable
print('9' in x)                    # retuns 'FALSE', the item is not present in the variable


# not in = Returns True if a sequence with the specified value is not present in the object.
y = ['harry', 'porter', 'blue', 'car']

print('chair' not in y)
print('blue' not in y)