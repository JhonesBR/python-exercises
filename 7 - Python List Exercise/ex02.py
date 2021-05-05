# Concatenate two lists index-wise
# Solution: https://github.com/JhonesBR

def concatList(l1, l2):
    concatedList = []
    for i in range(0, len(l1)):
        concatedList.append(l1[i]+l2[i])
    return concatedList


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
print(concatList(list1, list2))