import random
logo = '''

                                                                                                                                                                                                                      
                                                                                                                                                            bbbbbbbb                                                  
        GGGGGGGGGGGGG                                                                         NNNNNNNN        NNNNNNNN                                      b::::::b                                                  
     GGG::::::::::::G                                                                         N:::::::N       N::::::N                                      b::::::b                                                  
   GG:::::::::::::::G                                                                         N::::::::N      N::::::N                                      b::::::b                                                  
  G:::::GGGGGGGG::::G                                                                         N:::::::::N     N::::::N                                       b:::::b                                                  
 G:::::G       GGGGGuuuuuu    uuuuuu     eeeeeeeeeeee       ssssssssss      ssssssssss        N::::::::::N    N::::::uuuuuu    uuuuuu    mmmmmmm    mmmmmmm  b:::::bbbbbbbbb       eeeeeeeeeeee   rrrrr   rrrrrrrrr   
G:::::G             u::::u    u::::u   ee::::::::::::ee   ss::::::::::s   ss::::::::::s       N:::::::::::N   N::::::u::::u    u::::u  mm:::::::m  m:::::::mmb::::::::::::::bb   ee::::::::::::ee r::::rrr:::::::::r  
G:::::G             u::::u    u::::u  e::::::eeeee:::::ess:::::::::::::sss:::::::::::::s      N:::::::N::::N  N::::::u::::u    u::::u m::::::::::mm::::::::::b::::::::::::::::b e::::::eeeee:::::er:::::::::::::::::r 
G:::::G    GGGGGGGGGu::::u    u::::u e::::::e     e:::::s::::::ssss:::::s::::::ssss:::::s     N::::::N N::::N N::::::u::::u    u::::u m::::::::::::::::::::::b:::::bbbbb:::::::e::::::e     e:::::rr::::::rrrrr::::::r
G:::::G    G::::::::u::::u    u::::u e:::::::eeeee::::::es:::::s  ssssss s:::::s  ssssss      N::::::N  N::::N:::::::u::::u    u::::u m:::::mmm::::::mmm:::::b:::::b    b::::::e:::::::eeeee::::::er:::::r     r:::::r
G:::::G    GGGGG::::u::::u    u::::u e:::::::::::::::::e   s::::::s        s::::::s           N::::::N   N:::::::::::u::::u    u::::u m::::m   m::::m   m::::b:::::b     b:::::e:::::::::::::::::e r:::::r     rrrrrrr
G:::::G        G::::u::::u    u::::u e::::::eeeeeeeeeee       s::::::s        s::::::s        N::::::N    N::::::::::u::::u    u::::u m::::m   m::::m   m::::b:::::b     b:::::e::::::eeeeeeeeeee  r:::::r            
 G:::::G       G::::u:::::uuuu:::::u e:::::::e          ssssss   s:::::sssssss   s:::::s      N::::::N     N:::::::::u:::::uuuu:::::u m::::m   m::::m   m::::b:::::b     b:::::e:::::::e           r:::::r            
  G:::::GGGGGGGG::::u:::::::::::::::ue::::::::e         s:::::ssss::::::s:::::ssss::::::s     N::::::N      N::::::::u:::::::::::::::um::::m   m::::m   m::::b:::::bbbbbb::::::e::::::::e          r:::::r            
   GG:::::::::::::::Gu:::::::::::::::ue::::::::eeeeeeee s::::::::::::::ss::::::::::::::s      N::::::N       N:::::::Nu:::::::::::::::m::::m   m::::m   m::::b::::::::::::::::b e::::::::eeeeeeee  r:::::r            
     GGG::::::GGG:::G uu::::::::uu:::u ee:::::::::::::e  s:::::::::::ss  s:::::::::::ss       N::::::N        N::::::N uu::::::::uu:::m::::m   m::::m   m::::b:::::::::::::::b   ee:::::::::::::e  r:::::r            
        GGGGGG   GGGG   uuuuuuuu  uuuu   eeeeeeeeeeeeee   sssssssssss     sssssssssss         NNNNNNNN         NNNNNNN   uuuuuuuu  uuummmmmm   mmmmmm   mmmmmbbbbbbbbbbbbbbbb      eeeeeeeeeeeeee  rrrrrrr            
                                                                                                                                                                                                                      
                                                                                                                                                                                                                      
                                                                                                                                                                                                                      
                                                                                                                                                                                                                      
                                                                                                                                                                                                                      
                                                                                                                                                                                                                      
                                                                                                                                                                                                                      
'''
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
print(logo)

print("\nWelcome to Number guessing Game!")
print("\nTo guess a number between 1 to 100\n Easy have 10 chance to guess and Hard have 5 chances\n Good Luck")

game_type = input("Choose a difficulty. Type easy or hard : ")

if game_type.lower() == "easy":
    attempts = EASY_LEVEL_TURNS
elif game_type.lower() == "hard":
    attempts = HARD_LEVEL_TURNS
else:
    print("Enter either 'easy' or 'hard")

computer_number = random.randint(1,101)



def game(attempts):
    
    for i in range(attempts):
        print(f"You have {attempts-i} attempts remaining") 
        number = int(input("Make a guess: "))
        if i == attempts -1:
            str_append = "You lost"
        else:
            str_append = "Guess Again"
        if computer_number == number:
            print(f"Congratulation!!!, You Win, guessed number is {computer_number}")
            return
        if computer_number > number:
            if computer_number - number < 15:
                print(f"Your guess is low\n{str_append}")
            else:
                print(f"Your guess is too low\n{str_append}")
        if computer_number < number:
            if number - computer_number < 15:
                print(f"Your guess is high\n{str_append}")
            else:
                print(f"Your guess is too high\n{str_append}")

game(attempts)