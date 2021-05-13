# Below are the two lists convert it into the dictionary
# Solution: https://github.com/JhonesBR

def listsToDict(l1, l2):
    return dict(zip(l1, l2))


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print(listsToDict(keys, values))