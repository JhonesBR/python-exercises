# Reverse a given number and return true if it is the same as the original number
# Solution: https://github.com/JhonesBR

def reverseCheck(n):
    print(f"Original number {n}")
    if str(n)[::-1] == str(n):
        print("The original and reverse number is the same")
    else:
        print("The original and reverse number is not same")


n = int(input())
reverseCheck(n)