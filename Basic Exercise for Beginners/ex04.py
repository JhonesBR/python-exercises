# Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string
# Solution: https://github.com/JhonesBR

def removeChars(s, n):
    return s[n:]


s = input()
n = int(input())
newString = removeChars(s, n)
print(newString)