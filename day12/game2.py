import random
from art import logo

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5
turns =0

secret_number = random.randint(1,100)


def set_difficulty():
    global turns
    level = input("Enter the difficulty level 'Easy' or 'Hard' ")
    if level.lower() == 'hard':
        turns =  HARD_LEVEL_TURN
    else:
        turns = EASY_LEVEL_TURN
       
def check_answer(turns,number,secret_number):
    """ Check the number with secret_number and return turns """
    if number >secret_number:
        print("Too high")
        turns -=1
    elif number < secret_number:
        print("Too low")
        turns -=1
    else:
        print("You got this ! ")
        return 100 
    return turns 
    

def game():
    global turns
    print(logo)
    print("I am thinking about the number ")
    print("The number is between 1-100")
    set_difficulty()
    print(f"You have {turns} guess left.")

    while turns >0:

        
        number = int(input(">"))
        turns = check_answer(turns,number,secret_number)
        if turns == 100:
            break
        print(f"You have {turns} guess left . ")

        

        
        
    if turns ==0:
        print("You are run out of guess")
    else:
        print("You win!!")

game()
