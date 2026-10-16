#allows the computer to generate a random number between the specified range
import random

LOW, HIGH = 1, 50
MAX_ATTEMPTS = 10

#starts the game and prompts the user to guess the number, providing feedback with each guess
def play_game():
    secret = random.randint(LOW, HIGH)
    print(f"I'm thinking of a number between {LOW} and {HIGH}. You have {MAX_ATTEMPTS} attempts.")

    attempts = 0
    while attempts < MAX_ATTEMPTS:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter a number from {LOW} to {HIGH}: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not LOW <= guess <= HIGH:
            print(f"Please enter a number between {LOW} and {HIGH}.")
            continue

        attempts += 1
        
         #provides feedback to the user on their guess and whether it's too high, too low, or correct
        
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! Guessed it in {attempts} attempts.")
            return

    print(f"Out of attempts! The number was {secret}.")

play_game()

# calls for the function to start working and run the game