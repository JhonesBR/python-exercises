# Add a week (7 days) and 12 hours to a given date
# Solution: https://github.com/JhonesBR

from datetime import datetime, timedelta


given_date = datetime(2020, 3, 22, 10, 0, 0)
final_date = given_date + timedelta(days=7, hours=12)

print(f"given_data: {given_date}")
print(f"final_data: {final_date}")