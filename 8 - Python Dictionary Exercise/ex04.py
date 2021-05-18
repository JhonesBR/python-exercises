# Initialize dictionary with default values
# Solution: https://github.com/JhonesBR

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
final = dict.fromkeys(employees, defaults)
print(final)