# Display the cube of the number up to a given integer
# Solution: https://github.com/JhonesBR

def cubeToN(n):
    for i in range(1, n+1):
        print(f"{i}^3 = {i**3}")


cubeToN(6)