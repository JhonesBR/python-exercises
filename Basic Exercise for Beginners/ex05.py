# Given a list of numbers, return True if first and last number of a list is same
# Solution: https://github.com/JhonesBR
# Input numbers split by spaces (Ex: 10 20 30 40 10)

def firstLastSame(L):
    print(f"Given list is {L}")
    if L[0] == L[-1]:
        print("result is True")
    else:
        print("result is False")


L = input().split(" ")
firstLastSame(L)