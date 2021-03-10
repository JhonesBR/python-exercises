# Read line number 4 from the ex10.txt file
# Solution: https://github.com/JhonesBR

with open("ex10.txt", "r") as file:
    lines = file.readlines()
    try:
        print(f"Line 4: {lines[3]}")
    except:
        pass