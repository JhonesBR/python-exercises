# Check if a value 200 exists in a dictionary
# Solution: https://github.com/JhonesBR

def check200(d):
    return (200 in d.values() or 200 in d.keys())


sampleDict = {'a': 100, 'b': 200, 'c': 300}
print(check200(sampleDict))