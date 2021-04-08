# Remove special symbols/Punctuation from a given string
# Solution: https://github.com/JhonesBR

def removeSpecial(s):
    return "".join([c for c in s if (c.isalpha() or c == " ")])


s = "/*Jon is @developer & musician"
print(removeSpecial(s))