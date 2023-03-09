'''
The word to be guessed will be shown as List of "_", for example
if "user" is to guessed then word to be guessed will be shown as
["_","_","_","_"]
'''

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
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
wordlist = ["learning", "graduate", "welcome"]
word = random.choice(wordlist) # Choose a random word for wordlist
i= length = len(word)
output_word = [str("_")]*i # create a list with "_" of length each to word length

print(logo)
print(f"Word to Guess :  {output_word}")
while i!=0:
    
    user_choice = input("Guess a letter : ")
    counter = 0
    while counter < length:
        if user_choice == word[counter]:
            if output_word[counter] == "_":
                output_word[counter]=user_choice
                print(f"Guess Till Now is {output_word}")
                counter = length
                i-=1
        counter+=1
    if user_choice not in word:
        print(f"{user_choice}, not in the word")
        lives -= 1
        if lives == 0:
            i = 0
            print("You lose.")
    print(stages[lives])

if "".join(output_word) == word :
       print(f"Congratulation, you guessed correctly!!!!")