# Print multiplication table of a given number
# Solution: https://github.com/JhonesBR

def multiTable(n):
    for i in range(1, 11):
        print(n*i)


n = int(input("Insert a number: "))
multiTable(n)