import random

the_number = random.randint(1, 100)

EASY_TURNS = 10
HARD_TURNS = 5


def play_game(attempts):
    print(f"You have {attempts} attempts remaining to guess the number.")

    while attempts > 0:
        guess = int(input("Make a guess: "))

        if guess == the_number:
            print(f"You got it! The answer was {the_number}.")
            return
        attempts -= 1

        if guess > the_number:
            print("Too high!")
        else:
            print("Too low!")

        if attempts > 0:
            print("Guess again.")
            print(f"You have {attempts} attempts remaining to guess the number.")
        else:
            print("You've run out of guesses. Refresh the page to run again.")


print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level_of_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if level_of_difficulty == "easy":
    play_game(EASY_TURNS)
elif level_of_difficulty == "hard":
    play_game(HARD_TURNS)
