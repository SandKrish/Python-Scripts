import random

wordlist = ["learning", "graduate", "welcome"]
word = random.choice(wordlist)
output_word = ''
counter = 0
i = len(word)

while i != 0:
    
    user_choice_letter = input("Enter a Letter : ").lower()
    counter+=1
    if user_choice_letter == word[len(word)-i]:
        output_word +=word[len(word)-i]
        if i == 1:print(f"Congratulation, you guessed {output_word} correctly with {counter} guesses!!!")
        else:print(f"Right, word formation till now {output_word}")
        i -= 1
        
    else:
        print("Wrong, try again")