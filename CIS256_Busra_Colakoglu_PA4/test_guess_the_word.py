# Busra Colakoglu
# CIS256 Fall 2026
# Programming Assignment 4


from guess_the_word import (
    WORDS,
    choose_word,
    process_guess,
    display_word,
)


def test_choose_word():
    """Verify that the selected word belongs to the predefined list."""
    word = choose_word()
    assert word in WORDS


def test_correct_guess():
    """Verify that a correct guess is added to the guessed letters."""
    guessed_letters = set()

    correct, updated_letters = process_guess(
        "python", "p", guessed_letters
    )

    assert correct is True
    assert "p" in updated_letters


def test_incorrect_guess():
    """Verify that an incorrect guess does not reveal a letter."""
    guessed_letters = set()

    correct, updated_letters = process_guess(
        "python", "z", guessed_letters
    )

    assert correct is False
    assert "z" not in updated_letters


def test_repeated_letters():
    """Verify that all occurrences of a guessed letter are revealed."""
    guessed_letters = {"p"}

    result = display_word("apple", guessed_letters)

    assert result == "a p p _ _"


def test_display_word_hides_unguessed_letters():
    """Verify that unguessed letters remain hidden."""
    result = display_word("python", {"p", "o"})

    assert result == "p _ _ _ o _"


def test_invalid_guess():
    """Verify that invalid input does not change the guessed letters."""
    guessed_letters = {"p"}

    correct, updated_letters = process_guess(
        "python", "12", guessed_letters
    )

    assert correct is False
    assert updated_letters == {"p"}


def test_correct_guess_is_case_insensitive():
    """Verify that uppercase guesses work for lowercase words."""
    correct, updated_letters = process_guess(
        "python", "P", set()
    )

    assert correct is True
    assert "p" in updated_letters
