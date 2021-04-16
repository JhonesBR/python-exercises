# Iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element
# Solution: https://github.com/JhonesBR

def countElements(L):
    elements = {}
    for c in L:
        if c not in elements:
            elements[c] = L.count(c)
    return elements


L = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print(countElements(L))