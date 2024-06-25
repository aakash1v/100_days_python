
import random
import art
import os

clear = lambda : os.system('clear')

def deal_card():
    """Returns a random card from the deck."""
    cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]

    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards """

    if sum(cards) == 21 and len(cards) == 2:
        return 0 #blackjack`
    if 11 in cards and sum(cards) >21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score ==0:
        return "Lose, opponent has Blackjack "
    elif user_score ==0:
        return "Win with a Blackjack "
    elif user_score >21:
        return "you went over. You lose "
    elif computer_score > 21:
        return "Opponent went over . YOu win "
    elif user_score > computer_score:
        return "you win "
    else:
        return "You lose"
def play_game():

    print(art.logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
            
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards : {user_cards} and current score {user_score}")
        print(f" Computer's first card: {computer_cards[0]} ")


        if user_score==0 or computer_score == 0 or user_score >21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass : ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True


    #computer drawing cards ..
    while computer_score !=0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your cards : {user_cards} and your score is {user_score} ")
    print(f"Computer cards : {computer_cards} and computer score is { computer_score}")
    print(compare(user_score,computer_score))

play_game()
while input("Do you want to play a game of BlackJack ? type 'y' or 'n':") == 'y':
    clear()
    play_game()

