"""
try: The 'try' block lets you test a block of code for errors.
except: The 'except' block lets you handle the error.
else: The 'else' block lets you execute code when there is no error.
finally: The 'finally' block lets you execute code, regardless of the result of the try and except blocks.
"""


# Exception Handling:
try:
    print(x)                            # we don't have any value in the "x", still this code doesn't show the error
except:
    print("An exception occured!")



# Many Exeception:
try:
    print(y)
except NameError:
    print("Variable y is not defined!")          
except:
    print("Something else went wrong!")



# Else
try:
    print("Hello")
except:
    print("Something went wrong!")
else:
    print("Nothing went wrong!")        

# In this code both try and else statement run, because try block does not generate any eror.
# Also 'else' block lets you execute code when there is no error.


try:
    print(a)
except:
    print("Something went wrong!")      # In this code only except block is executed
else:
    print("Nothing went wrong!") 



# Finally
try:
    print(x)
except:
    print("Something went wrong!")
finally:
    print("The 'try except' is finished!")