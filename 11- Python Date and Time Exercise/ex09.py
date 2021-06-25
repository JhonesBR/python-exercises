# Calculate the date 4 months from the current date
# Solution: https://github.com/JhonesBR

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


given_date = given_date = datetime(2020, 2, 25).date()
final_date = given_date + relativedelta(months=4)

print(f"given_data: {given_date}")
print(f"final_data: {final_date}")