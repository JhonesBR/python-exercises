# Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
# Solution: https://github.com/JhonesBR
# Input numbers split by spaces (Ex: 10 20 33 46 55)

def divisible5(L):
    print("Divisible of 5 in a list")
    for i in L:
        if int(i)%5 == 0:
            print(i)


L = input().split(" ")
divisible5(L)