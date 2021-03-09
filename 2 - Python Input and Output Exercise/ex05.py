# Accept a list of 5 float numbers as an input from the user
# Solution: https://github.com/JhonesBR

numbers = []
for i in range(5):
    numbers.append(float(input(f"Insert number at index {i}: ")))

print(f"The list is {numbers}")