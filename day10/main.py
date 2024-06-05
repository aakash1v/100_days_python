

#Calculator..

#add
def add(n1,n2):
    return n1 + n2

#subtract
def sub(n1,n2):
    return n1 - n2

#multiplication
def multiply(n1,n2):
    return n1*n2

#division
def divide(n1,n2):
    return n1/n2

operations = {'+':add,'-':sub,'*':multiply,'/':divide}

function = operations['*']

num1 = int(input('What is the first number? :'))

for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input('What is the second number? :'))

function = operations[operation_symbol]
first_answer = function(num1,num2)
print(f"{num1} {operation_symbol} {num2} = {first_answer} ")

#second time operations..
while True:
    if not input(f"Type 'y' to continue calcualtion with {first_answer}, type 'n' to exit. ").lower().startswith('y'):
        break

    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    num3 = int(input("Enter the other number? :"))

    function = operations[operation_symbol]
    second_answer = function(first_answer,num3)
    print(f"{first_answer} {operation_symbol} {num3} = {second_answer} ")
    first_answer = second_answer
