# Given a number count the total number of digits in a number
# Solution: https://github.com/JhonesBR

def numberOfDigits(n):
    print(f"{n} has {len(str(n))} digits")


n = int(input("Insert a number: "))
numberOfDigits(n)