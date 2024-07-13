#list comprehension

numbers = [1,2,3]
new_list = [n+1 for n in numbers]
print(new_list)

name = 'Angela'
new_list = [letter for letter in name]
print(new_list)


new_list = [2*i for i in range(1,6)]
print(new_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_name = [name for name in names if len(name) <5]
print(short_name)



long_capital_name = [name.upper() for name in names if len(name) >4]
print(long_capital_name)
