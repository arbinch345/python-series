# capitalize() = converts first character to upper case.
a = "hello world!"

print(a.capitalize())


# casefold() = converts string into lower case. (same as lower())
a = "Hello WorlD!"

print(a.casefold())


# count() = returns the number of times specified value occurs in a string.
a = "Hello WorlD! Hello World! Bro,Hello"

print(a.count("Hello"))


# endswith() = Returns true if the string ends with the specified value.
a = "Hello WorlD! Hello World! Bro,Hello"

print(a.endswith("Hello"))
print(a.endswith("Bro"))


# startswith() = 
a = "Hello WorlD! Hello World! Bro,Hello"

print(a.startswith("Hello"))           # Returns true
print(a.startswith("Bro"))             # Returns False

# find() = searches the string passed in the parameter and returns the position/index of the value.
a = "Hello WorlD! Hello World! Bro,Hello"

print(a.find("Bro"))


# index() = same as find(). searches the string passed in the parameter and returns the position/index of the value.
a = "Hello WorlD! Hello World! Bro,Hello"

print(a.index("Bro"))


# isalnum() = Returns true if all characters in the string are alphanumeric.
a = "Mark124"

# txt = a.isalnum()
# print(txt)
print(a.isalnum())


# isalpha() = Returns True if all characters in the string are in the alphabet.
a = "Mark124"
b = "Bernal"

print(a.isalpha())          # Returns False
print(b.isalnum())          # Retruns True


# isdigit() = Returns True if all characters in the string are digits
a = "12345"

print(a.isdigit())


# isnumeric() = Same as isdigit(). Returns True if all characters in the string are numeric.
a = "12345"

print(a.isnumeric())


# islower() = 	Returns True if all characters in the string are lower case.
a = "hello"
b = "HQWER"

print(a.islower())              # Returns True
print(b.islower())              # Returns False


# isupper(): Returns True if all characters in the string are upper case
a = "hello"
b = "HQWER"

print(a.isupper())              # Returns False
print(b.isupper())              # Returns True


# istitle() = Returns True if the first letter of every word is capital.
a = "Mark, The Wonder Kid!"

print(a.istitle())


# join() = Joins the elements of an iterable to the end of the string
a = ("John", "Peter", "Vicky")

x = "*".join(a)

print(x)


# split() = Splits the string at the specified separator, and returns a list.
a = "Hello Bro"

print(a.split())


# strip() = reduce/trim the space. (rstrip, lstrip)
a = "           Hello, Bro"

print(a.strip())


# title() = Converts the first character of each word to upper case.
a = "hello! world"

print(a.title())


# swapcase(): swap lower to upper and upper to lower case.
a = "hELLO, Bro!"

print(a.swapcase())