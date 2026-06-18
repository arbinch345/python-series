# break statement: stop the condition even the condition is true.

i = 1

while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


# i = 0

# while i < 6:
#     i += 1
#     if i == 3:
#         break
#     print(i)

'''
prints only 2 because after that it adds 2 + 1 = 3, codition meets and break (comes out from the loop) and does not print or reads another line.
'''