import random
from hangman_word import random_english_words
from hangmanart import stages, logo

chosen_word = random.choice(random_english_words)

lives = 6

print(logo)

# testing code
# print(f"The solution is {chosen_word}") 

display = []
for x in range(len(chosen_word)):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    
    guessed_letter = input("Guess a letter: ").lower()

    if guessed_letter in display:
        print(f"You've already guessed letter: {guessed_letter}")

    for position in range(len(chosen_word)): # finding the position of the guessed letter
        letter = chosen_word[position] 
        # print(f"Current position: {position}\nCurrent letter: {letter}\nGuessed letter: {guessed_letter}")
        if letter == guessed_letter:
            display[position] = letter

    if guessed_letter not in chosen_word:
        print(f"You guessed {guessed_letter}, that's not in the word, You lose a life :( )")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
       
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    print(stages[lives])
    

        


