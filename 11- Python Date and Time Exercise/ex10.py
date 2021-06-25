# Calculate number of days between two given dates
# Solution: https://github.com/JhonesBR

from datetime import datetime, timedelta


date_1 = datetime(2020, 2, 25)
date_2 = datetime(2020, 9, 17)
print(f"{(date_2-date_1).days} days")