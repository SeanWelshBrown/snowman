import random
import os
from pyfiglet import figlet_format
from colorama import init
from termcolor import cprint

from words import words
from draw_snowman import draw_snowman


#~~ HELPER FUNCTIONS ~~#
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

def intro_message(word_in_progress):
    print()
    cprint(figlet_format('Snowman', font='big'), "blue", attrs=['bold'])
    cprint("Welcome to Snowman!\n", attrs=["bold"])
    print("You have 8 guesses before the snowman comes to life and wreaks havoc!\n")
    print("Your word:\n")
    bold_print(word_in_progress)
    print()

def bold_print(str, color=None):
    cprint(str, color, attrs=["bold"])


#~~ MAIN GAME ~~#
def snowman():
    # Game state
    word = get_word(words)
    word_in_progress = "_ " * len(word)
    wrong_letters = set()
    num_of_guesses = 0

    intro_message(word_in_progress)
    guess = input("Guess a letter to get started: ").upper()
    print()

    while "_" in word_in_progress or num_of_guesses < 8:
        os.system('clear')

        # Handle invalid guesses
        if len(guess) > 1:
            bold_print("Guess is too long. Guesses must be one letter only.\n")
        elif not guess.isalpha():
            bold_print("Invalid guess, guesses must be upper or lower case letters only (no numbers, symbols, etc.)\n")

        # Handle valid guesses
        elif guess in wrong_letters or guess in word_in_progress:
            bold_print(f"You've already guessed the letter {guess}. Try again!\n", "yellow")
        else:
            if guess in word:
                bold_print("Correct!\n", "green")
                word_in_progress = find_and_replace_letters(guess, word, word_in_progress)
            else:
                bold_print("Sorry, that letter isn't in the word. Try again!\n", "red")
                wrong_letters.add(guess)
        
        draw_snowman(len(wrong_letters))
        bold_print(word_in_progress)
        print()
        print()
        cprint("Wrong letters: \n{wrong_letters}\n".format(wrong_letters = ', '.join(wrong_letters)), "magenta", attrs=["bold"])
        guess = input("Guess another letter: ").upper()
        print()

    print()
    print("You guessed the word!\n")
    print(f"The word was '{word.capitalize()}'\n")

    if input("Play again? [Y / N]: ").upper() == "Y":
        snowman()
    else:
        print("Thanks for playing!\n")


## RUN THE PROGRAM ##
init()
os.system('clear')
snowman()


# print(u'\u2500' * 30)