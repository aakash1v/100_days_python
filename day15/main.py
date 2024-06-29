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



money = 0

while True:
    clear()
    print(logo)
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_choice.lower() =='off':
        break
    

    # TODO: 3. Print report.
    if user_choice.lower() == 'report':
        for key in resource:
            print(key, resource[key])
        stopper()
        continue

    if user_choice not in MENU.keys():
        print("please select the correct option..\n")
        hidden_option()
        stopper()
        continue
    coffee = MENU[user_choice]



    # TODO: 4. Check resources sufficient?
    # a. When the user chooses a drink, the program should check if there are enough
    # resources to make that drink.
    # b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
    # not continue to make the drink but print: “Sorry there is not enough water.”
    # c. The same should happen if another resource is depleted, e.g. milk or coffee.
    has_sufficient_ingredients = True
    for key in coffee['ingredients']:
        if resource[key] < coffee['ingredients'][key]:
            print(f"Sorry there is not enough {key} ")
            has_sufficient_ingredients = False

    if has_sufficient_ingredients:
        for key in coffee['ingredients']:
            resource[key] = resource[key]- coffee['ingredients'][key]
    else:
        hidden_option()
        stopper()
        continue


    # TODO: 5. Process coins.
    # a. If there are sufficient resources to make the drink selected, then the program should
    # prompt the user to insert coins.
    # b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    # c. Calculate the monetary value of the coins inserted. E.g
    total =0
    print("Please insert coins.")

    total += int(input("how many quarters :"))*.25
    total += int(input("how many dimes :"))*.10
    total += int(input("how many nickles :"))*.05
    total += int(input("how many pennies :"))*.01
    
    
    # TODO: 6. Check transaction successful?
    if coffee['cost'] > total:
        print("Sorry this is not enough money, Money refunded.")
    else:
        print("Here is $%.2f in change."%(total - coffee['cost']))
        money = coffee['cost']
        

    # TODO: 7. Make Coffee.
    print(f"Here is your {user_choice} Enjoy.\n")
    stopper()
    

     


