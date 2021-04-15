# Given two lists create a third list by picking an odd-index element from the first list and even index elements from the second.
# listOne = [3, 6, 9, 12, 15, 18, 21]
# listTwo = [4, 8, 12, 16, 20, 24, 28]
# Solution: https://github.com/JhonesBR

def mixList(l1, l2):
    L = []
    for i in range(len(l1)):
        if i%2 == 1:
            L.append(l1[i])
    for i in range(len(l2)):
        if i%2 == 0:
            L.append(l2[i])
    return L


listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
print(mixList(listOne, listTwo))