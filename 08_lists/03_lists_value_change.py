# To change the value of specific item, we use index number.

the_list = ["apple", "orange", "cherry", "grapes"]
the_list[1] = "watermelon"                            # replace the value
print(the_list)


# change the range of item values
my_list = ["apple", "orange", "cherry", "grapes"]
my_list[0:3] = ["mango", "berry", "raspberry"]    
print(my_list)                                        # replace the item from range 0 to 2 (position 3rd is not included)


# If you insert less items than you replace, the new items will be inserted where you specified
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) 


# insert() : insert the item without replacing any value.
list = ["apple", "banana", "cherry"]
result = list.insert(1, "berry")
print(result)
# print(list.insert(2, "raspberry"))               # modifies directly to the list so it prints "none"


