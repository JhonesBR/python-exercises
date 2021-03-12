# Reverse the following list using for loop
# list1 = [10, 20, 30, 40, 50]
# Solution: https://github.com/JhonesBR

def reverseList(L):
    newList = []
    for i in range(len(L)-1, -1, -1):
        newList.append(L[i])
    print(f"Reversed List: {newList}")


list1 = [10, 20, 30, 40, 50]
reverseList(list1)