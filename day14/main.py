import random
from game_data import data
import art
import os
clear = lambda: os.system("clear")

def game(score):
    
    print(art.logo)
    if score> 0:
        print(f"You are right your current score is {score}.")
   
    a = random.randint(0,49)
    b = random.randint(0,49)

    print(f'Compare A: {data[a]["name"]} a {data[a]["description"]} from {data[a]["country"]}.')
    print(art.vs)
    print(f'Compare B: {data[b]["name"]} a {data[b]["description"]} from {data[b]["country"]}.')

    user_answer = input("Who has more followers ? Type 'A' or 'B' ")
    
    if data[a]["follower_count"]> data[b]["follower_count"]:
        answer = 'a'
    else:
        answer = 'b'
    if user_answer.lower() == answer:
        return 1
    else:
        return -1




score =0 
while True:
    clear()
    new_score = game(score)

    if new_score ==-1:
        print(f"Sorry that is wrong. Final score is {score}.")
        break

    score +=new_score




