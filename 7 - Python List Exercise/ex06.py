# Remove empty strings from the list of strings
# Solution: https://github.com/JhonesBR

def removeEmpty(l):
    return [i for i in l if i != ""]


list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print(removeEmpty(list1))