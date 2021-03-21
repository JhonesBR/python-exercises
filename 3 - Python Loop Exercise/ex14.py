# Reverse a given integer number
# Solution: https://github.com/JhonesBR

def reverse(n):
    print(f"Given: {n}\nReversed: {str(n)[::-1]}")


n = int(input("Insert a number to reverse: "))
reverse(n)