# Write a program to display all prime numbers within a range
# Solution: https://github.com/JhonesBR

def primeRange(start, end):
    for i in range(start, end+1):
        isPrime = True
        for j in range(2, i):
            if i%j == 0:
                isPrime = False
        if isPrime:
            print(i)

start = 25
end = 50
primeRange(start, end)