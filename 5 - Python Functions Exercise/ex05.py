# Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it
# Solution: https://github.com/JhonesBR

def outerFunction(a, b):
    def innerFunction(a, b):
        return a+b
    tmp = innerFunction(a, b)
    return tmp+5
    

print(outerFunction(5, 10))