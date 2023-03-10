def prime_checker(number):
    counter = 2
    for i in range(2,number):
        if number%i != 0 :
            counter+=1   
        else:
            i = number
    if counter == number:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(n)