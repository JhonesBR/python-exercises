# Convert string into a datetime object
# Solution: https://github.com/JhonesBR

from datetime import datetime


string = "Feb 04 2020  9:15AM"
data = datetime.strptime(string, '%b %d %Y %I:%M%p')
print(data)