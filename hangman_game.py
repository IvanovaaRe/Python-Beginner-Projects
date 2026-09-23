secret_word = "apple"
guess = ""
guessed_letters = []
while True:
    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word)
    if "_" not in display_word:
        print("You win!")
        break
