# Given a list, remove the element at index 4 and add it to the 2nd position and at the end of the list
# list1 = [54, 44, 27, 79, 91, 41]
# Solution: https://github.com/JhonesBR

def L4(L):
    L = L[:2] + [L[4]] + L[2:] + [L[4]]
    return L


list1 = [54, 44, 27, 79, 91, 41]
print(L4(list1))