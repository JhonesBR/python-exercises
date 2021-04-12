# Write a recursive function to calculate the sum of numbers from 0 to 10
# Solution: https://github.com/JhonesBR

def func(n):
    if n == 1:
        return n
    else:
        return n + func(n-1)


print(func(10))