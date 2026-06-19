# Upper Case: upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())


# Lower Case: lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())


# Remove Whitespace: the space before and/or after the actual text, and very often you want to remove this space.

# strip(): removes any whitespace from the beginning or the end:

a = " Hello, World!  "
print(a.strip())


# replace (): replaces a string with another string.

a = "Hello, World!"
print(a.replace("H", "M"))


# split(): splits the string into substrings if it finds instances of the separator.

a = "Hello, World!"
print(a.split(","))


# f-string: used in formatting and interpolation (formatted string) {}

price = 10.99

print(f"This item costs ${price}")