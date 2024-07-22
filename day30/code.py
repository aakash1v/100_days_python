#FileNotFound error
#try:
#    file = open('a_file.txt')
#    a_dictionary  ={'key':'value'}
#    print(a_dictionary['asef'])
#except FileNotFoundError:
#    file = open('a_file.txt', 'a')
#    file.write('Something')
#except KeyError as error_message:
#    print(f'The key {error_message} does not exist.')
#else:
#    content = file.read()
#    print(content)
#finally:
#    raise TypeError('This is the error that I made up.')

height = float(input('height: '))
weight = int(input('weight: '))

if height > 3:
    raise ValueError('Human height should not be over 3 meter.')

bmi = weight /height **2
print(bmi)
