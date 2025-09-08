import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")

    number_to_guess = random.randint(1, 100)
    attempts = 0
    Game_number = []
    user_number = []
    Game_number.append(number_to_guess)

    while True:
        guess = input("Enter your guess: ")
        user_number.append(guess)

        # check if input is a number
        if not guess.isdigit():
            print("Please enter a valid number")
            continue
        if int(guess) > 100:
            print("Please enter number between 1 to 100")
            continue


        guess = int(guess)
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed the number in {attempts} tries.")
            print(f"{Game_number} Game Number")
            print(f"{user_number} The list of Your Number")
            break

        if abs(guess - number_to_guess) <= 10:
            print("You're very close! Within 10 numbers.")

number_guessing_game()
