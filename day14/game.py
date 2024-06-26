import random
from art import logo,vs
from game_data import data
import os
clear = lambda : os.system("clear")

score =0
#generate a random account from data

a = random.randint(0,49)
b = random.randint(0,49)

a_data = data[a]
b_data = data[b]


while True:
    clear()
    #display logo
    print(logo)
    # formate the account data into printable formate
    compare_a = f"Compare A: {a_data["name"]} , a {a_data["description"]}, from {a_data["country"]} . "
    compare_b = f"Compare B: {b_data["name"]} , a {b_data["description"]}, from {b_data["country"]} . "

    #printing the score..
    if score >0:
        print(f"You are right ! your score is {score} ")
    print(compare_a)
    print(vs)
    print(compare_b)
    # ask user for a guess.
    guess = input("Who has more follower ? Type 'A' or 'B' . ")

    # check if user is correct
    ## get follower count of each account
    ## use if satement to check if user is correct
    follower_a = a_data["follower_count"]
    follower_b = b_data["follower_count"]

    if follower_a > follower_b:
        answer = 'a'
    else:
        answer = 'b'

    # Give user feedback on their guess
    if guess.lower() == answer:
        score +=1

    else:
        print(f"Sorry that is wrong . Your final score is {score} . ")
        break

    # making the account at position B become the next account at position A
    a_data =  b_data
    
    b = random.randint(0,49)
    b_data  = data[b]
    
# score keeping

# make the game repetable


# clear the screen between the round

