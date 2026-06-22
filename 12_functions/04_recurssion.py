# recursion = when a function calls itself 
# base case = a condition that stops the recursion
# recursive case = the function calling itself with a modified argument

def factorial(n):
    # base case
    if n == 1 or n == 0:
        return 1
    # recursive case
    else:
        return n * factorial(n - 1)

print(factorial(5))


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))



def sum_list(numbers):
    if len(numbers) == 1:
        return numbers[0]
    
    else:
        return numbers[0] + sum_list(numbers[1:])
    
my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))
