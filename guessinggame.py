import random
import math
import os

random_int = random.randint(1,10)


#Ask the user for its guess


def guessing():
    guess = int(input("What do you think the number is?: "))
    if guess < random_int:
        print(str(guess) + " is too low\n")
        guessing()
    if guess > random_int:
            print(str(guess) + " is too high\n")
            guessing()
    if guess == random_int:
        print(str(guess) + " was the correct answer!")
        


guessing()
    

