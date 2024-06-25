import random

secret_number = random.randint(1,100)
print("Guess the number between 1-100")
difficulty = input("Enter the difficulty level 'Easy' or 'Hard' ")

if difficulty.lower() =='hard':
    guess = 5
else:
    guess = 10

while guess >0:
    
    number = int(input(">"))
    if number >secret_number:
        print("Too high")
    elif number < secret_number:
        print("Too low")
    else:
        print("You got this ! ")
        break
    guess -=1
    print(f"You have {guess} guess left . ")

if guess ==0:
    print("YOu are run out of guess.. ")
else:
    print("YOu win!!")

