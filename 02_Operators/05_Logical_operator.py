# Logical operator are used to combine conditional statements:

# and = Returns 'True' if both statements are true
x = 5

print(3 < 5 and x < 7)
# Here both condition are true. (3 is smaller than x(5) and less than 10.)


# or = Returns True if one of the statments is 'True'
y = 7

print(4 < y  or y < 6)                # Here only one condition is true


# not = Reverse the result, returns False if the result is true
z = 9

print(not(z))             # returns 'False', the result is true
print(not(z < 5 and z > 7))    