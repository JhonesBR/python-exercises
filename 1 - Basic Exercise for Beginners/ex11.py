# Write a code to extract each digit from an integer, in the reverse order
# Solution: https://github.com/JhonesBR

def reverseSplit(n):
    s = [c for c in n[::-1]]
    print(" ".join(s))


n = input()
reverseSplit(n)