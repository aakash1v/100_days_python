from menu import MENU,resource
import os
logo ="""
________._________
|      | \   -   /
|  ||  |  \  -  /
|  ||  |___\___/
|  ||  |     X
|      |    ___
|      |   / - \\
|______|  /  -  \\
| ____ | /_______\\
||7:30||__________
||____|           |
|_________________|
"""


clear = lambda : os.system('clear')
hidden_option = lambda : print("press 'report' for report and 'off' to off the coffee machine ")
def stopper(): 
    tmp = input("press 'Enter' to continue the process... ")

class Coffee:

    def __init__(self):
        self.menu = MENU
        self.resource = resource

    def report(self):
        for key,value in self.resource.items():
            print(f"{key} : {value} ")
    
    def check_resource(self,name,reduce_resource=False):
        ingredients_dict =  self.menu[name]['ingredients']
        enough_resource = True

        for item in ingredients_dict:
            if ingredients_dict[item] > self.resource[item]:
                print(f"Sorry their is no enough {item}. ")
                enough_resource = False
            else:
                # processing the coffee and subtracting the resources..
                if reduce_resource ==True:
                    self.resource[item] -= ingredients_dict[item]

        return enough_resource

    def process_coin(self):
        total =0
        print("Please Enter number of coines")
        total += int(input("How many number of quarters :"))*.25
        total += int(input("How many number of dimes :"))*.10
        total += int(input("How many number of nickles :"))*.05
        total += int(input("How many number of pennies :"))*.01
        return total

    def make_coffee(self):
        eligible_for_coffee = False
        name = input("What would you like? (espresso/latte/cappuccino).")
        
        #report..
        if name.lower() == 'report':
            self.report()
        elif name.lower() =='off':
            return False

        elif name in self.menu.keys():
            # checking resource...
            if self.check_resource(name):
                coffee_price = self.menu[name]['cost']
                price_paid = self.process_coin()
                
                if price_paid > coffee_price:
                    print("Here is %.2f in change "%(price_paid -coffee_price))
                    eligible_for_coffee = True
                else:
                    print("This is not enough money, money refunded")

            #giving the coffee..
            if eligible_for_coffee:
                self.check_resource(name,True)
                print(f"Here is your {name} .Enjoy \n")

        else:
            print("Please select the right option...")

            




# Driver code
coffee = Coffee()

while True:
    clear()
    print(logo)
    check = coffee.make_coffee()
    if check == False:
        break
    stopper()

