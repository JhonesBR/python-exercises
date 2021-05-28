# Return a set of all elements in either A or B, but not both
# Solution: https://github.com/JhonesBR

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1.symmetric_difference(set2)
print(set3)