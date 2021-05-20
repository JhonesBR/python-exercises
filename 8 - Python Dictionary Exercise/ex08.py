# Rename key city to location in the following dictionary
# Solution: https://github.com/JhonesBR

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sampleDict["location"] = sampleDict.pop("city")
print(sampleDict)