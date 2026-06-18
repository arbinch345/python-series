# continue statement: It stops the current iteration and continue from next step

i = 0

while i < 6:
    i += 1
    
    if i == 3:
        continue
    print(i)

i = 1

# while i < 6:
#     print(i)
    
#     if i == 3:
#         continue
#     i += 1

'''
continues the loop. First it prints 1 and 2. Then at number 3, it gets stucked and skip below code and continues printing 3. 
'''