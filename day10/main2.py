import art
import os


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


def calculator():
    should_continue = True
    
    print(art.logo)
    num1 = float(input('What is the first number? :'))
    while should_continue:

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input('What is the next  number? :'))

        function = operations[operation_symbol]
        answer = function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer} ")

        choice = input(f"Type 'y' to continue calculating with {answer}  and 'n' to start a new calculation (any other key to exit) :").lower() 
        if choice =='y':
            num1 = answer
        elif choice.lower() =='n':
            should_continue = False
            os.system('clear')
            calculator()
        else:
            print("The End.")
            return 
        
calculator()
