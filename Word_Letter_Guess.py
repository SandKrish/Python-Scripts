import random

wordlist = ["learning", "graduate", "welcome"]
word = random.choice(wordlist) # Choose a random word for wordlist
i= length = len(word)
output_word = [str("_")]*i # create a list with "_" of length each to word length

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

if "".join(output_word) == word :
       print(f"Congratulation, you guessed correctly!!!!")