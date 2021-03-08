# Print multiplication table form 1 to 10
# Solution: https://github.com/JhonesBR

def multiTable():
    for i in range(1, 11):
        print(f"{i}  ", end="")
        for j in range(2, 11):
            print(f"{i*j} ", end="")
        print()


multiTable()