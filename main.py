import random
from hangman_words import word_list
from hangman_art import stages, logo
import os

display = []

# TODO-8
lives = 6

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess.
# Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# TODO-4 - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"]
# with 5 "_" representing each letter to guess

# TODO-5 Loop through each position in the chosen_word;
# If the letter at that position matches guess then
# reveal that letter in the display at that position.
# e.g If the user guessed "p" and the chosen word was
# "apple", then display should be ["_", "P", "P", "_", "_"]

# TODO-6: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

# TODO-7: - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").
# Then you can tell the user they've won.

# TODO-8: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.

# TODO-9: - If guess is not a letter in the chosen_word,
# Then reduce 'lives' by 1.
# If lives goes down to 0 then the game should stop and it should print "You lose."

# TODO-10: - print the ASCII art from 'stages' that corresponds
# to the current number of 'lives' the user has remaining.

# TODO-1
chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)


# TODO-4
for _ in range(word_length):
    display.append("_")

print(logo)
print(f"the chosen word is: {chosen_word}")


def guess_letter():
    global lives

    if not lives:
        # TODO-10
        print(stages[lives])
        print("You lose.")
        lives -= 1
        return

    # TODO-2
    guess = input("Guess a letter from the word: ").lower()

    if guess.upper() in display:
        print("You already guessed this letter")
        return

    # TODO-5
    for position in range(word_length):
        char = chosen_word[position]

        # TODO-3
        if guess == char:
            display[position] = char.upper()

    if guess not in chosen_word:
        # TODO-9
        print("That's not in the word. You lose a life.")
        print(stages[lives])
        lives -= 1

    if "_" not in display:
        print(f"{' '.join(display)}")
        print("You win")
    else:
        # TODO-6
        print(f"{' '.join(display)}")

    return lives


# TODO-7
while "_" in display and lives >= 0:
    guess_letter()
