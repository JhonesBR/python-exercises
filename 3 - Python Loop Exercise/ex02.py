# Print the following pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
# Solution: https://github.com/JhonesBR

for i in range(1, 6):
    for j in range(0, i):
        print(f"{i} ", end="")
    print()