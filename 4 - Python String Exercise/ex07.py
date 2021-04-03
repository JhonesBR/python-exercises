# String characters balance Test
# We’ll assume that a String s1 and s2 is balanced if all the chars in the s1 are there in s2. characters’ position doesn’t matter.
# Solution: https://github.com/JhonesBR

def balance(s1, s2):
    for c in s1:
        if not c in s2:
            return False
    return True


print(balance("Yn", "PYnative"))
print(balance("Ynf", "PYnative"))