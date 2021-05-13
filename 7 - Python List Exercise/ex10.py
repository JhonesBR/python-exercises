# Given a Python list, remove all occurrence of 20 from the list
# Solution: https://github.com/JhonesBR

def remove20(l):
    return [i for i in l if i != 20]


list1 = [5, 20, 15, 20, 25, 50, 20]
print(remove20(list1))