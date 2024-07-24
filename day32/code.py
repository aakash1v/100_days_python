import datetime as dt

now = dt.datetime.now()
year = now.year
month= now.month
day = now.day
day_of_week = now.weekday()

date_of_birth = dt.datetime(year=2003, month =8, day=8)
print(date_of_birth)
