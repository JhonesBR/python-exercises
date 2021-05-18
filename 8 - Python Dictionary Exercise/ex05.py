# Create a new dictionary by extracting the following keys from a below dictionary
# Solution: https://github.com/JhonesBR

def getKeys(d, keys):
    finalDict = {}
    for key in keys:
        finalDict.update({key : d[key]})
    return finalDict


sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
keys = ["name", "salary"]

print(getKeys(sampleDict, keys))