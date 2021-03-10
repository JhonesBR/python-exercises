# How to check file is empty or not
# Solution: https://github.com/JhonesBR

def checkEmpty(file):
    if len(file.readlines()) == 0:
        return "empty"
    else:
        return "not empty"

# Not empty file
state = checkEmpty(open("ex09_data.txt", "r"))
print(f"File ex09_data.txt is {state}")

# Empty file
state = checkEmpty(open("ex09_empty.txt", "r"))
print(f"File ex09_empty.txt is {state}")