#file = open('my_file.txt')
#
#contents = file.read()
#print(contents)
#file.close()

with open('../../test.txt',mode='r') as file:
    print(file.read())
