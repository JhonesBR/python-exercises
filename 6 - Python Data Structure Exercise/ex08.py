# Iterate a given list and Check if a given element already exists in a dictionary as a key’s value if not delete it from the list
# Given
# rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
# sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
# Solution: https://github.com/JhonesBR

def func(sampleDict, rollNumber):
    new = [i for i in rollNumber if i in sampleDict.values()]
    print(f"New list: {new}")


rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

func(sampleDict, rollNumber)