# Given a string, display only those characters which are present at an even index number.
# Solution: https://github.com/JhonesBR

def printEvenChars(s):
    print(f"Original String is {s}")
    print("Printing only even index chars")
    for i in range(len(s)):
        if i%2 == 0:
            print(s[i])


s = input()
printEvenChars(s)