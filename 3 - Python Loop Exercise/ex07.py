# Print the following pattern using for loop
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1
# Solution: https://github.com/JhonesBR

for i in range(6):
    for j in range(5-i, 0, -1):
        print(f"{j} ",end="")
    print()