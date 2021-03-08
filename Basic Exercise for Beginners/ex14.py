# Print downward Half-Pyramid Pattern with Star (asterisk)
# Solution: https://github.com/JhonesBR

def starPattern():
    for i in reversed(range(6)):
        for j in range(i):
            print("* ", end="")
        print()


starPattern()