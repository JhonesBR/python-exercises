# Assign a different name to function and call it through the new name
# Solution: https://github.com/JhonesBR

def func(name, age):
    print(f"Name: {name}\nAge: {age}")


func("Jhones", "19")
newFunc = func
newFunc("Jhones", "19")