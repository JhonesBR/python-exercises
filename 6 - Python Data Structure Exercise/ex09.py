# Exercise 9: Given a dictionary get all values from the dictionary and add them to a list but don’t add duplicates
# Solution: https://github.com/JhonesBR

def listFromDict(d):
    myList = []
    for i in d.values():
        if i not in myList:
            myList.append(i)
    return myList


speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
print(listFromDict(speed))