# Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# Solution: https://github.com/JhonesBR

def concatAll(l1, l2):
    final = []
    for x in l1:
        for y in l2:
            final.append(x+y)
    return final


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
print(concatAll(list1, list2))