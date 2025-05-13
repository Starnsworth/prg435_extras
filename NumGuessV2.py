#    Program to guess a number from 1 to 100 in least tries using higher or lower messages to the user.
import random

def gen_target(lower,upper):
    target = random.randint(lower,upper)
    return target

def guess():
    lower = 1
    upper = 100
    i = 0
    correct = False
    print("Welcome to the Number Guessing Game!")
    val = gen_target(lower,upper)
    while not correct:
        i += 1
        userinput = int(input(f"Enter a number between {lower} and {upper}: "))
        if userinput == val:
            print(f"Congratulations, you guessed it in {i} tries!")
        elif userinput < val:
            print("Sorry, you guessed too low.")
        elif userinput > val:
            print("Sorry, you guessed too high.")


guess()