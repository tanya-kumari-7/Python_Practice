""" Number Guessing Game
User guesses a number between 1–100.
Program gives hints (“too high”, “too low”).
Helps with random module, conditions, loops.
"""

import random

print("Hi there!! :)")
print("Welcome to a Fun Game: Number Guessing")

def guessing_game_fun():
    game_num = random.randint(1, 100)
    attempt = 0
    check = False
    
    while not check:
        user_num = int(input("Please guess the number between 1-100: "))
        attempt += 1

        if user_num > game_num:
            print(f"Too high! Try again. Attempt: {attempt}")
        elif user_num < game_num:
            print(f"Too low! Try again. Attempt: {attempt}")
        else:
            print(f" Congratulations! You guessed it in {attempt} attempts.")
            check = True

guessing_game_fun()