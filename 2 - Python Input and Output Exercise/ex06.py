# Write all content of a given file into a new file by skipping line number 5
# Solution: https://github.com/JhonesBR

with open("ex06.txt", "r") as txt:
    lines = txt.readlines()
    for i in range(len(lines)):
        if i != 4:
            print(lines[i])