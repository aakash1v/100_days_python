import pandas
import numpy

#data = pandas.read_csv('weather_data.csv')
#print(type(data))
#print(type(data['temp']))
#
#data_dict = data.to_dict()
#print(data_dict)
#temp_list = data['temp'].to_list()

#avg = numpy.average(temp_list)
#print(avg)
#print(numpy.sum(temp_list))

#print(data['temp'].mean())
#print(data['temp'].max())

# Get data in Row
#print(data[data.temp == data.temp.max()])

#def cel_to_far(x):
#    return x*9/5 + 32
#
#monday = data[data.day =='Monday']
#print(cel_to_far(monday.temp))

# create a dataframe from scratch..

#data_dict ={
#        'students': ['Any','James','Angela'],
#        'scores' : [76, 56, 65]
#        }
#data = pandas.DataFrame(data_dict)
#data.to_csv('new_data.csv')

data = pandas.read_csv('squirrel_data.csv')
all_squirrel = data['Primary Fur Color'].to_list()
black = all_squirrel.count('Black')
cinnamon = all_squirrel.count("Cinnamon")
grey = all_squirrel.count('Gray')

squirrel_count_dict = {
        'Fur Color':['Black','Cinnamon','Grey'],
        'Count':[black, cinnamon , grey],
        }

#print(squirrel_count_dict)
data = pandas.DataFrame(squirrel_count_dict)
data.to_csv('squirrel_count.csv')
