import random
import Hangman_stages
import Hangman_words

print(Hangman_stages.logo)

chosen_word = random.choice(Hangman_words.words)

display = []

for _ in range(len(chosen_word)):
    display += "_"
print(display)

end_game = False

lives = 6

while not end_game: 
    guess = input("User guess letter: ")

    if guess in display:
        print("You have already guessed!")

    for x in range(len(chosen_word)):
        if guess == chosen_word[x]:
            display[x] = chosen_word[x]

    if guess not in chosen_word:
        print(f"{guess} is not in the word, you lose a live.")
        lives -= 1
        print(f"Lives left: {lives}")
        if lives == 0:
            end_game = True
            print("You lost!")


    print(f"{''.join(display)}")
    
    if "_" not in display:
        end_game = True
        print("You won!")

    print(Hangman_stages.stages[lives])