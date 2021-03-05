# Given a range of the first 10 numbers, Iterate from the start number to the end number, and In each iteration print the sum of the current number and previous number
# Solution: https://github.com/JhonesBR

for i in range(10):
    if i == 0:
        n = 0
    else:
        n = i-1
    print(f"Current Number {i} Previous Number {n}  Sum: {i+n}")