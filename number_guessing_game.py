import random

numbers = range(1,101)
the_number = random.choice(numbers)



def easy_level():
    attempts = 10
    if level_of_difficulty == "easy":
            print("You have 10 attempts remaining to guess the number.")
    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess > the_number and attempts > 0:
            attempts = attempts - 1
            if attempts == 0:
                print("You've run out of guesses. Refresh the page to run again.")
                break
            else:
                print("Too high!")
                print("Guess again.")
                print(f"You have {attempts} attempts remaining to guess the number.")
        if guess < the_number and attempts > 0:
            attempts = attempts - 1
            if attempts == 0:
                print("You've run out of guesses. Refresh the page to run again.")
                break
            else:
                print("Too low!")
                print("Guess again.")
                print(f"You have {attempts} attempts remaining to guess the number.")
        if guess == the_number:
            print(f"You got it! The answer was {the_number}.")
            break


def hard_level():
    attempts = 5
    if level_of_difficulty == "hard":
        print("You have 5 attempts remaining to guess the number.")
    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess > the_number and attempts > 0:
            attempts = attempts - 1
            if attempts == 0:
                print("You've run out of guesses. Refresh the page to run again.")
                break
            else:
                print("Too high!")
                print("Guess again.")
                print(f"You have {attempts} attempts remaining to guess the number.")
        if guess < the_number and attempts > 0:
            attempts = attempts - 1
            if attempts == 0:
                print("You've run out of guesses. Refresh the page to run again.")
                break
            else:
                print("Too low!")
                print("Guess again.")
                print(f"You have {attempts} attempts remaining to guess the number.")
        if guess == the_number:
            print(f"You got it! The answer was {the_number}.")
            break


print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level_of_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level_of_difficulty == "easy":
    easy_level()
if level_of_difficulty == "hard":
    hard_level()
