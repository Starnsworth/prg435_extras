#    Program to guess a number from 1 to 5.
import random

def gen_target(lower,upper):
    target = random.randint(lower,upper)
    return target

def guess():
    lower = 1
    upper = 5
    i = 0
    correct = False
    print("Welcome to the Number Guessing Game!")
    val = gen_target(lower,upper)
    while not correct:
        i += 1
        userinput = int(input(f"Enter a number between {lower} and {upper}: "))
        if userinput == val:
            print(f"Congratulations, you guessed it in {i} tries!")
        else:
            print("Sorry, try again.")


guess()