# To check certain phrase or character in strings or not, you can use these syntax

txt = "Hello, My name is Mack. I'm a programmer."

if "programmer" in txt:                 # Here I have used "in" to check the word.
    print("present!")
else:
    print("NOt present!")


txt = "Hello, My name is Mack. I'm a programmer."

if "Bob" not in txt:
    print("Not present!!")
else:
    print("present!")


# Looping Through a strings:

for x in "banana":
    print(x)