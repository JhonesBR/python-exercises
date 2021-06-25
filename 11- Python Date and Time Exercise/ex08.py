# Convert the following datetime into a string
# Solution: https://github.com/JhonesBR

from datetime import datetime


given_date = datetime(2020, 2, 25)
string = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(string)