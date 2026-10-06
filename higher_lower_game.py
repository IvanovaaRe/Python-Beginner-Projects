import random

from art import logo
from art import vs
from game_data import data


def compare(person_a, person_b):
    if person_a["follower_count"] > person_b["follower_count"]:
        winner = person_a
        return winner
    else:
        winner = person_b
        return winner

print(logo)
current_score = 0
game_over = False

person_a = random.choice(data)
person_b = random.choice(data)

while not game_over:
    while person_a == person_b:
        person_b = random.choice(data)

    name_a = person_a["name"]
    description_a = person_a["description"]
    country_a = person_a["country"]
    print(f"Compare A: {name_a}, a/an {description_a}, from {country_a}.")

    print(vs)

    name_b = person_b["name"]
    description_b = person_b["description"]
    country_b = person_b["country"]
    print(f"Against B: {name_b}, a/an {description_b}, from {country_b}.")

    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    winner = compare(person_a, person_b)

    if answer == "A" and winner == person_a:
        current_score += 1
        print(f"You are right! Current score: {current_score}.\n")
        person_a = person_b
        person_b = random.choice(data)

    elif answer == "B" and winner == person_b:
        current_score += 1
        print(f"You are right! Current score: {current_score}.\n")
        person_a = person_b
        person_b = random.choice(data)

    else:
        print(f"Sorry, that's wrong. Final score: {current_score}.")
        game_over = True
