# Given a string of odd length greater than 7, return a new string made of the middle three characters of a given String
# Solution: https://github.com/JhonesBR

def middleThree(s):
    cut = int((len(s)-3)/2)
    return s[cut:cut+3]


s = "JhonDipPeta"
print(middleThree(s))