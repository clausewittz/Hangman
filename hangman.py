import random
import hangman_art
from hangman_art import stages
from hangman_words import word_list


print(hangman_art.logo)
chosen_word = random.choice(word_list)
game_over = False
lives = 6

display = []


for letter in chosen_word:
    display += "_"
print(display)


while game_over == False:
    guess = input("Guess a letter:").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if guess == letter:
            display[position] = guess

    if guess in chosen_word:
        print(f"Your current live:{lives}")

    if guess not in chosen_word:
        lives -= 1
        print(f"You lose a life:{lives}")
        if lives == 0:
            print(f"You lose. The word was:{chosen_word}")
            game_over = True

    print(display)

    if "_" not in display:
        game_over = True
        print("You win")

    print(stages[lives])
