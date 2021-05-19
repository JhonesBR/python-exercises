# Delete set of keys from a dictionary
# Solution: https://github.com/JhonesBR

def removeKeys(d, keys):
    finalDict = {}    
    for key in d.keys() - keys:
        finalDict.update({key: d[key]})
    return finalDict


sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
  
}
keysToRemove = ["name", "salary"]
print(removeKeys(sampleDict, keysToRemove))