f = open("demo.txt", 'r')
# data = f.read()

# print(data)
print(f.read())


# find the word "methods" from the demo.txt
file = open('demo.txt', 'r')

data = file.read()

if "methods" in data:
    print("Word found!")
else:
    print("Not found!")


