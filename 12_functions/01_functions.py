# functions: block of code which runs when it is called
#            created using "def" keyword.

def my_function():
    print("Hello bro's!")

my_function()              # --> function has been called here and can call same function multiple times
my_function()


# Why use function: write the code once and reuse it.

def add_num(a, b):
    add = a + b
    print(add)

add_num(2, 4)
add_num(100, 19998)


# Return Values: it send the data back to the code and stores it as a variable.
#                when a function reaches a return statement, it stops executing and sends the result back.


def get_greeting():
    return "Hello from a function!"

message = get_greeting()                 # --> stores the value in message variable
# print(get_greeting(message))
print(message)


def add(a, b):
    return a + b

x = add(2, 3)
y = x + 10
z = add(x, y)

print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")


# Pass Statement: It is used when you code latter. Functions should not be empty so "pass" statement is used.

def sub():
    pass

# You can code it later.