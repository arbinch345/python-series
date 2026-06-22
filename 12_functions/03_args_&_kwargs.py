# *args and *kwargs allow functions to accept a unknown number of arguments

# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments

def add(a, b):
    return a + b

print(add(1,2))

def my_func(*args):
    total = 0
    for arg in args:
        total += arg
    return total
    
print(my_func(5, 4, 5))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr.", "Hari", "Bahadur", "karki")



def address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
address(street="234 fake st",
        apt="100",
        city="ktm",
        zip="4404")



# Using both *args & **kwargs
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if 'apt' in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('city')}, {kwargs.get('province')}")


shipping_label("Dr.", "Hari", "Bahadur", "karki",
               street='123 fake st',
            #    apt='#199',
               city='ktm',
               province='Gandaki')