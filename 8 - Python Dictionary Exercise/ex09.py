# Get the key of a minimum value from the following dictionary
# Solution: https://github.com/JhonesBR

def getMin(d):
    return min(d, key=sampleDict.get)


sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(getMin(sampleDict))