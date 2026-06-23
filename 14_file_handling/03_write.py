file = open("deport.txt", "w")          # open new file and write there

file.write("Hello! Here i can write it because i have open the file in write mode")


# overwrite the content of file
f = open("deport.txt", "w")

f.write("I have overwrite this text file")

# to read the overwritten file
f = open("deport.txt", "r")

print(f.read())