# Given two integer numbers return their product. If the product is greater than 1000, then return their sum
# Solution: https://github.com/JhonesBR

n1 = int(input())
n2 = int(input())

product = n1*n2
if product > 1000:
    print(f"The result is {n1+n2}")
else:
    print(f"The result is {product}")