# Given a Python list of numbers. Turn every item of a list into its square
# Solution: https://github.com/JhonesBR

def turnToSquare(L):
    for i in range(len(L)):
        L[i] = L[i]**2
    return L


aList = [1, 2, 3, 4, 5, 6, 7]
print(turnToSquare(aList))