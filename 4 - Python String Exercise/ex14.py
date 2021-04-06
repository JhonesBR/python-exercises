# Remove empty strings from a list of strings
# Solution: https://github.com/JhonesBR

def removeEmpty(s):
    s = list(filter(None, s))
    return ([c for c in s if (c.isdigit() or c.isalpha())])


strList = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print(removeEmpty(strList))