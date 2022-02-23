
"""
training with import datetime
"""

import datetime
#  date in format
birthday = datetime.date(2022, 12, 18)
#  date now
tday = datetime.date.today()
# date delta, which adds the desired number of days to the given date
tdelta = datetime.timedelta(days=10)

till_bith = tday - birthday

print(birthday)
print(tday)
print(tday + tdelta)
print(till_bith)