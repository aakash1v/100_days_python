import hangman_words
import hangman_art
import random


the_word = random.choice(hangman_words.word_list)
n = len(the_word)
display= ['_']*n
n = len(the_word)
lives = 6


#testing ..
print(f'Psst, the solution is {the_word}.')
end_of_game = False
print(hangman_art.logo)

while not end_of_game:
    
    guess = input('Enter the letter :').lower()
    for i in range(n):
        letter = the_word[i]
        if guess ==letter: 
            display[i] = letter 
    print(''.join(display))

    if guess not in the_word:
        lives -=1
        if lives ==0:
            print('You lose')
            end_of_game = True


    if '_' not in display:
       end_of_game = True
       print(display)
       print('You win')

    print(hangman_art.stages[lives])



