# Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1
# Solution: https://github.com/JhonesBR

def middleMerge(s1, s2):
    cut = int(len(s1)/2)
    merged = s1[:cut] + s2 + s1[cut:]
    return merged


s1, s2 = "Ault", "Kelly"
print(middleMerge(s1, s2))