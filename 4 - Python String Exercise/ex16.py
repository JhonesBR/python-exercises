# Removal all the characters other than integers from a string
# Solution: https://github.com/JhonesBR

def removeChars(s):
    return "".join([c for c in s if c.isdigit()])


s = "I am 25 years and 10 months old"
print(removeChars(s))