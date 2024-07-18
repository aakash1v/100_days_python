def add(*args):
    return sum(args)


#print(add(1,2,3,4,5))

#    print(type(kwargs))
def calculate(n, **kwargs):

    #for key,value in kwargs.items():
        #print(key)
        #print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)



#calculate(2, add =3, multiply= 5)

class Car:

    def __init__(self,**kw):
        self.make = kw.get('make')
        self.model = kw.get('model')


new_car = Car(make = 'NIsan')
print(new_car.make)
