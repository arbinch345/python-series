# Python argument: information can be passed into functions which is denoted by parenthesis () called arguments.

# funtion with one argument

def my_function(fname):            # --> Argument is called inside ()
    print(f"My name is {fname}")

my_function("Mack")                # --> function called


# Note: Argument/parameter are almost same thing.

#  Argument: actual value that is sent to the function when it is called
# parameter: the variable listed inside the parentheses in the function definition

def my_func(name):                 # --> name is parameter
    print(f"Hello {name}")

my_func("Mark")                    # --> "Mark" is an argument sent to function



# two arguments (which one is correct between these two: )

# def my_function(fname, lname):
#     print(f"{fname} {lname}")

# my_function("Emily", "Dickinson")



# def my_function(fname, lname):          
#     print(f"{fname} {lname}")

# my_function("Emily")                # --> one function arguments is called, so throws error



# Default parameter values: If the function is called without an argument, it uses the default value.

def function(name = "fready"):
    print(f"Hello {name}")

function()              # print "Hello fready"
function("Emily")       # print "Hello Emily"


# Keyword argument: You can send arguments with key = value syntax

def keyword(animal, name):
    print(f"I have a {animal}.")
    print(f"My {animal} name is {name}.")

keyword(animal= "dog", name = "Buddy")


# Positional Arguments: when you call a function with arguments without usign keywords, they are called positional arguments.
#                       It must be in the correct order.

def keyword(animal, name):
    print(f"I have a {animal}.")
    print(f"My {animal} name is {name}.")

keyword(animal= "dog", name = "Buddy")

def keyword(animal, name):
    print(f"I have a {animal}.")
    print(f"My {animal} name is {name}.")

keyword(animal= "Buddy", name = "Dog")


# Mixing Positional and keyword Argument: passing different data arguments.

def my_function(animal, name, age):
    print(f"I have a {age} year old {animal} named {name}")

my_function("dog", name = "Buddy", age = 5)


def my_function(animal, name, age):
    print(f"I have a {age} year old {animal} named {name}")

# my_function(name = "Buddy", age = 5, "dog")                     # --> Throws error as the position is not correct.
