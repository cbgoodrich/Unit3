#Charlie Goodrich
#09/28/17
#numberGuessingGame.py - makes you guess a random number, tells you the number of tries

from random import randint

number = randint(1,100)
guessAttempts = 1
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number:
        print("Guess higher")
    elif guess > number:
        print("Guess lower")
    else:
        break
    print("It only took you", guessAttempts, "tries to get it")
    guessAttempts += 1
