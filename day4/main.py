
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print('-'*70)
print('***************Welcome to my Rock-Paper-Scissor game *****************')
print('-'*70)

game_images = [rock,paper,scissors]

user_choice =''
total_game =0
total_win =0

while(user_choice !=-1): 
	user_choice = int(input("What do u choose? Type 0 for Rock, 1 for Paper and 2 for scissors.(-1 to exit) "))

	if user_choice>=3 or  user_choice <0:
		print("YOu type and Invalid number u lose")
	else:
		print("User choice :")
		print(game_images[user_choice])

	computer_choice = random.randint(0,2)
	print("Computer choice :")
	print(game_images[computer_choice])

	if user_choice>=3 or user_choice <0:
		print('The End')
	elif computer_choice == user_choice :
		print("It's a draw")
	elif user_choice==0:
		if computer_choice ==1:
			print('You Lose!')
		else:
			print('YOu win!')
			total_win +=1

	elif user_choice==1:
		if computer_choice ==2:
			print('You Lose!')
		else:
			print('YOu win!')
			total_win +=1
	else:
		if computer_choice ==0:
			print('You Lose!')
		else:
			print('YOu win!')
			total_win +=1
	total_game +=1


print('Total game played :',total_game)
print(f"YOur total point :{total_win}")
print('Thank YOu!')
