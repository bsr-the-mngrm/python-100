from art import logo
from os import system
import random

def input_difficulty():
    """Returns the user's difficulty choice"""
    input_str = "Choose a difficulty. Type 'easy' or 'hard': "
    difficulty = input(input_str)
    while difficulty.lower() != "easy" and difficulty.lower() != "hard":
        difficulty = input("Wrong answer! " + input_str)
    return difficulty.lower()

def input_guess():
    """Returns the user's guess"""
    input_str = "Make a guess: "
    guess = input(input_str)
    while not guess.isnumeric():
        guess = input("Only numbers are acceptable! " + input_str)
    return int(guess)

def input_wants_to_play():
    """Returns 'y' or 'n' depending on whether the user wants to play or not."""
    input_str = "Do you want to play again? Type 'y' to continue or type 'n' to exit: "
    wants_to_play = input(input_str)
    while wants_to_play.lower() != "y" and wants_to_play.lower() != "n":
        wants_to_play = input("Wrong answer! " + input_str)
    return wants_to_play.lower()

def check_the_guess(random_number, guess):
    """Checks the guess whether it equals the random number or not."""
    if guess > random_number:
        print("Too high.")
        return False
    elif guess < random_number:
        print("Too low.")
        return False
    else:
        print("Equal!")
        return True

def play_game():
    system("cls||clear")
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1,100)
    is_guessed = False

    difficulty = input_difficulty()

    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5

    while attempts != 0 and not is_guessed:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = input_guess()

        if check_the_guess(random_number=random_number, guess=guess):
            is_guessed = True
        else:
            attempts -= 1 

    if is_guessed:
        print(f"I thought on {random_number}. You guessed the number! Nice job!")
    else:
        print(f"I thought on {random_number}. You missed! Better luck next time!")

wants_to_play = 'y'

while wants_to_play.lower() == 'y':
    play_game()
    wants_to_play = input_wants_to_play()