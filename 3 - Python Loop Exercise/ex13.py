# Display Fibonacci series up to 10 terms
# Solution: https://github.com/JhonesBR

def fat(n):
    if n == 0:
        print("0! = 1")
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial = factorial * i
        print(f"{n}! = {factorial}")


fat(10)