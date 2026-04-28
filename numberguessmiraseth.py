import random

def get_guess():
    while True:
        guess = input("Enter a guess from 1 to 100: ")

        if guess.isdigit():
            guess = int(guess)

            if 1 <= guess <= 100:
                return guess

        print("Invalid input. Try again.")


def play_game():
    secret_number = random.randint(1,100)
    attempts = 0
    guesses = []

    print("Welcome to the Number Guessing Game!")

    while True:
        guess = get_guess()

        if guess in guesses:
            print("You already guessed that number.")
            continue

        guesses.append(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low!")

        elif guess > secret_number:
            print("Too high!")

        else:
            print("Correct! You guessed the number.")
            print("It took you", attempts, "attempts.")
            break


play_game()