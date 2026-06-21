# You cannot access set by referring to an index or key. 

set_a = {'apple', 'mango', 'banana'}

for x in set_a:
    print(x)


# Checking with 'in' and 'not in'

set_b = {'apple', 'cherry', ' mango', 'grapes', 'banana'}

print('apple' in set_b)
print('cherry' not in set_b)