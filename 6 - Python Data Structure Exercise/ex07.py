# Given two sets, Checks if One Set is a subset or superset of another Set. if the subset is found delete all elements from that set
# Solution: https://github.com/JhonesBR

def subOrUp(s1, s2):
    if s1.issubset(s2):
        s1.clear()
    if s2.issubset(s1):
        s2.clear()
    print(f"First Set: {s1}\nSecond Set: {s2}")


firstSet = {27, 43, 34}
secondSet = {34, 93, 22, 27, 43, 53, 48}
subOrUp(firstSet, secondSet)