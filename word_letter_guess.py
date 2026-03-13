"""
Simple Word Guess Game

The program randomly selects a word from a list.
The word is displayed as underscores.

Example:
If the word is "user", it will appear as
_ _ _ _

The player guesses letters until the full word is revealed.
"""

import random

# List of possible words
word_list = ["learning", "graduate", "welcome"]

# Choose a random word
word = random.choice(word_list)

# Length of the word
length = len(word)

# Create a list of blanks
output_word = ["_"] * length

print("Word to Guess:", " ".join(output_word))

remaining_letters = length

# Continue until all letters are guessed
while remaining_letters != 0:

    user_choice = input("Guess a letter: ")

    counter = 0

    # Check each letter of the word
    while counter < length:

        if user_choice == word[counter]:

            if output_word[counter] == "_":
                output_word[counter] = user_choice

                print("Guess Till Now:", " ".join(output_word))

                counter = length
                remaining_letters -= 1

        counter += 1


# Check if word was guessed correctly
if "".join(output_word) == word:
    print("Congratulations! You guessed the word correctly!")
