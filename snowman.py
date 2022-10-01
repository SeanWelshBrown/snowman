import random
import os
from pyfiglet import figlet_format
from colorama import init
from termcolor import cprint

from words import words
from draw_snowman import draw_snowman


# HELPER FUNCTIONS
def get_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()

def find_and_replace_letters(letter, word, word_in_progress):
    letter_indexes = [i for i in range(len(word)) if word[i] == letter]
    word_arr = word_in_progress.split()
    for i in letter_indexes:
        word_arr[i] = letter

    return " ".join(word_arr)

def is_valid_guess(guess):
    while True:
        if len(guess) > 1:
            print("Guess is too long. Guesses must be one letter only.\n")
        elif not guess.isalpha():
            print("Invalid guess, guesses must be upper or lower case letters only (no numbers, symbols, etc.)\n")
        else:
            return guess.upper()

        guess = input("Please guess again: ")
        print()


# MAIN GAME FUNCTION
def snowman():
    word = get_word(words)
    word_in_progress = "_ " * len(word)
    guessed_letters = {
        "wrong": set(),
        "right": set()
    }

    os.system('clear')

    print()
    cprint(figlet_format('Snowman', font='big'), attrs=['bold'])
    print("Welcome to Snowman!\n")
    print("You have 9 guesses before the snowman comes to life and wreaks havoc!\n")
    print("Your word:\n")
    print(word_in_progress)
    print()
    guess = is_valid_guess(input("Guess a letter to get started: "))
    print()

    while True:
        if guess in guessed_letters["wrong"] or guess in guessed_letters["right"]:
            print(f"You've already guessed the letter {guess}. Try again!\n")
        else:
            if guess in word:
                print("Correct!\n")
                word_in_progress = find_and_replace_letters(guess, word, word_in_progress)
                guessed_letters["right"].add(guess)
            else:
                print("Sorry, that letter isn't in the word. Try again!\n")
                guessed_letters["wrong"].add(guess)

        if "_" in word_in_progress:
            os.system('clear')
            
            print(u'\u2500' * 30)
            draw_snowman(len(guessed_letters["wrong"]))
            print(word_in_progress)
            print()
            print("Wrong guesses: {wrong_letters}\n".format(wrong_letters = ', '.join(guessed_letters["wrong"])))

            guess = is_valid_guess(input("Guess another letter: "))
            print()
        else:
            break

    print(u'\u2500' * 30)
    print()
    print("You guessed the word!\n")
    print(f"The word was '{word.capitalize()}'\n")

    if input("Play again? [Y / N]: ").upper() == "Y":
        print(u'\u2500' * 30)
        snowman()
    else:
        print("Thanks for playing!\n")


# RUN THE PROGRAM
init()
snowman()