'''
Identity operators are used to compare the objects, not if they are 
equal, but if they are actually the same object with the same memory 
location.
'''


# is = Returns "True" if both variables are the same object
x = 6
y = 5
z = x

print(x is z)                        # Retun "TRUE", the value of z is same as x
print(y is z)                        # Return "False", they are not same



# is not = Returns True if both variables are not the same object.
a = 9
b = a
c = 5

print(a is not c)
print(a is not b)