# Write a function called "exponent(base, exp)" that returns an int value of base raises to the power of exp.
# Solution: https://github.com/JhonesBR

def exponent(base, exp):
    print(f"{base} raises to the power of {exp} is: {base**exp}")


base = int(input())
exp = int(input())
exponent(base, exp)