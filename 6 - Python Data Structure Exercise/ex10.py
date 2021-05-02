# Remove duplicate from a list and create a tuple and find the minimum and maximum number
# Solution: https://github.com/JhonesBR

def func(L):
    unique = list(set(L))
    myTuple = tuple(L)
    minN = min(myTuple)
    maxN = max(myTuple)
    print(f"Unique: {unique}\nTuple: {myTuple}\nMinimum: {minN}\nMaximum: {maxN}")


sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
func(sampleList)