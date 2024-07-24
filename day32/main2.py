from datetime import datetime
import pandas

today = datetime.now()
data  = pandas.read_csv('birthdays.csv')

birthdays_dict = {(data_row['month'], data_row['day']) :data_row  for (index, data_row) in data.iterrows()}
print(birthdays_dict)
