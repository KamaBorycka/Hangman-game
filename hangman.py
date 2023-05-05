from random import choice

from hangman_art import logo, stages
from hangman_words import word_list

lives = 6
playing = True
display = []

print(logo)

choosen_word = choice(word_list)

for character in choosen_word:
    display += "_"
print(display)

while playing:
    guess = input("Guess a letter: ").lower()

    for position in range(len(choosen_word)):
        letter = choosen_word[position]

        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in choosen_word:
        print(
            f"You guessed a letter:{guess}, that's not in the word. You lose one life"
        )
        lives -= 1

        if lives == 0:
            playing = False
            print("You loose")
            print(f"The correct answer was: {choosen_word}")
        print(stages[lives])

    if "_" not in display:
        playing = False
        print("You win")
