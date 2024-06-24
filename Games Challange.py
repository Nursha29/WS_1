#!/usr/bin/env python

import random

def main():
    """Start a polygon guessing game."""
    print("Guess the polygon!")
    
    shapes = [
        "square",
        "pentagon",
        "triangle",
        "hexagon",
        "heptagon",
        "octagon",
        "nonagon",
        ]
    
    x =random.choice(shapes)
    max_trials= 3
    trial=0
    guess = None
    #print(x)
    while trial<max_trials:
        guess = str(input("What a polygon are we thinking of? "))
        
        if x == guess:
            print(f"You guessed.Congratulations you got it right!".format(guess))
            break
        else:
            print(f"Unfortunately you got the wrong answer.".format(guess))
            print(f"You have {max_trials} chances remaining.")
            max_trials -= 1
        if max_trials == 0:
            print(f"out of attempts. The polygon is actually {x}.".format(guess))
        
main()