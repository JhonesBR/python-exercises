# Given a list, iterate it, and display numbers divisible by five, and if you find a number greater than 150, stop the loop iteration
# Solution: https://github.com/JhonesBR

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for n in list1:
    if n%5 == 0:
        print(n)
    if n == 150:
        break