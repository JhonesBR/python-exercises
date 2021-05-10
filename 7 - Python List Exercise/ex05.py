# Given a two Python list. Iterate both lists simultaneously such that list1
# should display item in original order and list2 in reverse order
# Solution: https://github.com/JhonesBR

def func(l1, l2):
    for i in range(len(l1)):
        print(l1[i], l2[len(l2)-1-i])


list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
func(list1, list2)