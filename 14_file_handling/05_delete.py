import os
# os access our operating sys

# os.remove("report.txt")                     # you can also use this simple method

if os.path.exists("report.txt"):
    os.remove("report.txt")
    print("File deleted!")
else:
    print("No such file exists!")