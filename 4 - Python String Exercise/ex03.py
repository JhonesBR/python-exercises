# Given two strings, s1, and s2 return a new string made of the first, middle, and last characters each input string
# Solution: https://github.com/JhonesBR

def merge(s1, s2):
    first = s1[0] + s2[0]
    middle = s1[int(len(s1)/2)] + s2[int(len(s2)/2)]
    final = s1[len(s1)-1] + s2[len(s2)-1]
    return first + middle + final


s1, s2 = "America", "Japan"
print(merge(s1, s2))