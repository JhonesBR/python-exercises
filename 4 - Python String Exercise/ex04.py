# Arrange string characters such that lowercase letters should come first
# Solution: https://github.com/JhonesBR

def lowerFirst(s):
    lowers, uppers = [], []
    for c in s:
        if c.islower():
            lowers.append(c)
        else:
            uppers.append(c)
    return "".join(lowers) + "".join(uppers)


s = "PyNaTive"
print(lowerFirst(s))