# Create a function showEmployee() in such a way that it should accept employee name, and its salary and display both.
# If the salary is missing in the function call assign default value 9000 to salary
# Solution: https://github.com/JhonesBR

def showEmployee(name, salary=9000):
    print(f"{name} salary is {salary}")


showEmployee("Jhones", "10000")
showEmployee("Jhones")