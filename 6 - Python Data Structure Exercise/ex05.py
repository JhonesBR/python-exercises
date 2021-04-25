# Given a two list of equal size create a Python set such that it shows the element from both lists in the pairGiven a two list of equal size create a Python set such that it shows the element from both lists in the pair
# Solution: https://github.com/JhonesBR

def makePairs(l1, l2):
    return [(l1[i], l2[i]) for i in range(len(l1))]


l1 = [2, 3, 4, 5, 6, 7, 8]
l2 = [4, 9, 16, 25, 36, 49, 64]
print(makePairs(l1, l2))