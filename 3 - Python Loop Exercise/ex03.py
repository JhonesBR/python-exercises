# Accept number from user and calculate the sum of all number from 1 to a given number
# Solution: https://github.com/JhonesBR

def sumToN(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    print(f"Sum from 1 to {n} = {sum}")


n = int(input("Insert a number: "))
sumToN(n)