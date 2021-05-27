# Remove items 10, 20, 30 from the following set at once
# Solution: https://github.com/JhonesBR

set1 = {10, 20, 30, 40, 50}

set1.difference_update({10, 20, 30})
print(set1)