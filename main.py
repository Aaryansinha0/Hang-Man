import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)

from hang import word_list
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6


#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f"You have already used this letter {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if letter != chosen_word:
      print
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("you lose!")
        
    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win.")

    from stages import stages
    print(stages[lives])
