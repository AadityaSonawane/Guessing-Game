import random

print("   Number Guessing Game")
guessedNumber = int(input("Guess a number between 1 and 9: "))
randomNumber = random.randint(1,9)
guessCount = 0

while guessCount<5:
    if(guessedNumber == randomNumber):
        print("Congratulations!!!")
        break
    else:
        if(abs(guessedNumber-randomNumber)<=2):
            print("You were close, ", end="")
        else:
            print("The number you guessed is too far, ", end="")
        guessedNumber = int(input("Enter a number greater than " + str(guessedNumber) + ": "))
        randomNumber = random.randint(randomNumber, 9)
    guessCount+=1
if(guessCount == 5):
    print("You lose!!!")
