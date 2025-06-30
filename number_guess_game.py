guess=int(input("Now you can start guessing the number!!!"))
secret_number=67
while guess!=secret_number:
    if(guess>secret_number):
        print("Too high!! Try again")
        guess=int(input("Guess again!!"))
    else:
        print("Too low!! Try again")
        guess=int(input("Guess again!!"))
print("Yes, You guessed it right!!!")