# Subtract a week (7 days)  from a given date in Python
# Solution: https://github.com/JhonesBR

from datetime import datetime, timedelta


given_date = datetime(2020, 2, 25)
final_date = given_date - timedelta(days=7)

print(f"given_data: {given_date}")
print(f"final_data: {final_date}")