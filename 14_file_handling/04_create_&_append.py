# f = open("demo1.txt", 'x')       # This will create the file demo1.txt


# write and append somthing in this file
file = open("demo1.txt", "w")

file.write("This file is used for demo purpose.")

# appendt
file = open("demo1.txt", "a")

file.write("Append this sentence.")

# read
# with open("demo1.txt", 'r') as f:
#     print(f)


file = open("demo1.txt")

print(file.read())