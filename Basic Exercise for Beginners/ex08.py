# Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5
# Solution: https://github.com/JhonesBR

def pattern():
    for i in range(1, 6):
        for j in range(i):
            print(f"{i} ", end="")
        print()


pattern()