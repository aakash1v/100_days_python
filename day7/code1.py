import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark","baboon","camel"]

the_word = random.choice(word_list)
n = len(the_word)
display= ['_']*n
n = len(the_word)
lives = 6

print('--------- The is Hangman game ----------------\n')
print('Guess the secret word ')


print(f'Psst, the solution is {the_word}.')
end_of_game = False

while not end_of_game:
    print(*display)
    
    guess = input('Enter the letter :').lower()
    for i in range(n):
        letter = the_word[i]
        if guess ==letter: 
            display[i] = letter 

    if guess not in the_word:
        lives -=1
        print(stages[lives])
        if lives ==0:
            print('You lose')
            end_of_game = True


    if '_' not in display:
       end_of_game = True
       print(display)
       print('You win')




