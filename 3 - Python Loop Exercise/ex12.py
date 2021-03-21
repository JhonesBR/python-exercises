# Write a loop to find the factorial of any number
# Solution: https://github.com/JhonesBR

def fib(n):
    n1, n2 = 1, 1
    for i in range(n):
        print(n1, end="  ")
        tmp = n1 + n2
        n1 = n2
        n2 = tmp

fib(10)