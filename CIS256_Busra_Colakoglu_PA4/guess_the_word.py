# Busra Colakoglu
# CIS256 Fall 2026
# Programming Assignment 4

import random

# The game randomly selects one word from this predefined list.
WORDS = ["python", "computer", "programming", "developer", "keyboard"]


def choose_word():
    """Return a randomly selected word from the predefined list."""
    return random.choice(WORDS)


def process_guess(word, guess, guessed_letters):
    """Check a guess and update the set of correctly guessed letters."""
    guess = guess.lower()

    # Only accept a single alphabetic character.
    if len(guess) != 1 or not guess.isalpha():
        return False, guessed_letters

    # Add the guess only if it appears in the secret word.
    if guess in word:
        guessed_letters.add(guess)
        return True, guessed_letters

    return False, guessed_letters


def display_word(word, guessed_letters):
    """Show correctly guessed letters and hide the remaining letters."""
    # Every occurrence of a correctly guessed letter is revealed.
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )


def play_game():
    """Run the word guessing game until the player wins or loses."""
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = set()
    max_attempts = 6

    print("Welcome to the Word Guessing Game!")
    print("Guess the word one letter at a time.")

    # Continue while attempts remain and the word is not fully revealed.
    while len(incorrect_guesses) < max_attempts:
        print("\nWord:", display_word(word, guessed_letters))
        print("Incorrect guesses:", sorted(incorrect_guesses))
        print("Attempts remaining:", max_attempts - len(incorrect_guesses))

        guess = input("Enter one letter: ").strip().lower()

        # Reject invalid input without using an attempt.
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue

        # Do not penalize the player for repeating a guess.
        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed that letter.")
            continue

        correct, guessed_letters = process_guess(
            word, guess, guessed_letters
        )

        if correct:
            print("Correct guess!")
        else:
            incorrect_guesses.add(guess)
            print("Incorrect guess!")

        # Check whether every letter has been revealed.
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return

    # The player loses after six incorrect guesses.
    print("\nGame over! The word was:", word)


# Start the game only when this file is run directly.
if __name__ == "__main__":
    play_game()
