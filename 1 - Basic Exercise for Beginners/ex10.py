# Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list
# Solution: https://github.com/JhonesBR
# Input numbers split by spaces (Ex: 10 20 23 11 17 and 13 43 24 36 12)

def merge(L1, L2):
    newList = []
    for i in L1:
        if int(i)%2 != 0:
            newList.append(i)
    for i in L2:
        if int(i)%2 == 0:
            newList.append(i)
    print(f"Result List is {newList}")


L1 = input().split(" ")
L2 = input().split(" ")
merge(L1, L2)