# Check if all items in the following tuple are the same
# Solution: https://github.com/JhonesBR

def allEqual(t):
    first = t[0]
    for i in t:
        if i != first:
            return False
    return True


tuple1 = (45, 45, 45, 45)
print(allEqual(tuple1))