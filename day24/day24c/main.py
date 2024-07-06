#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
    

names=[]
with open('./Input/Names/invited_names.txt', mode='r') as file:
    for line in file.readlines():
        names.append(line.strip())

with open('./Input/Letters/starting_letter.txt',mode='r') as file:
    letter = file.readlines()


for name in names:
    letter[0] = f"Dear {name},\n"
    new_letter = ''.join(letter)  # converting letter in list to letter in string
    with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w') as file:
        file.write(new_letter)

