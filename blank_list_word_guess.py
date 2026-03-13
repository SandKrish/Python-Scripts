"""
The word to be guessed is displayed as a list of "_".
Example:
If the word is "user", it will appear as
["_", "_", "_", "_"]
"""

import random

wordlist = ["learning", "graduate", "welcome"]
word = random.choice(wordlist) # Choose a random word from the word list
length = len(word)
i= length
output_word = ["_"] * i # Create a list of "_" with the same length as the word

print(f"Word to Guess :  {output_word}")
# Continue the game until the word is guessed
while i!=0:
    
    user_choice = input("Guess a letter : ")
    counter = 0
    # Check each letter of the word
    while counter < length:
        if user_choice == word[counter]:
            if output_word[counter] == "_":
                output_word[counter]=user_choice
                print(f"Guess Till Now is {output_word}")
                counter = length
                i-=1
        counter+=1

if "".join(output_word) == word :
       print("Congratulations! You guessed the word correctly!")
