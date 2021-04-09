# Write a function func1() such that it can accept a variable length of argument and print all arguments value
# Solution: https://github.com/JhonesBR

def func1(*args):
    for arg in args:
        print(arg)


func1(10, 20, 30, 40, 50, "a", "b")