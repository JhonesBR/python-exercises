# Find the last position of a substring “Emma” in a given string
# Solution: https://github.com/JhonesBR

def lastEmmaOccurence(s):
    return s.rfind("Emma")


s = "Emma is a data scientist who knows Python. Emma works at google."
print("Last occurrence of Emma starts at", lastEmmaOccurence(s))