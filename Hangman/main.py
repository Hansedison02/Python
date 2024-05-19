import random
import os

def letter_checker(word, letter_check, guessed_letters):
    result = []
    for i in range(len(word)):
        if word[i] == letter_check:
            if i == 0:
                result.append(letter_check.upper())
            else:
                result.append(letter_check)
        elif word[i] in guessed_letters:
            if i == 0:
                result.append(word[i].upper())
            else:
                result.append(word[i])
        else:
            result.append("_")
    return "".join(result)

word_list = ["aardvark", "thylacine", "quokka", "rabbit", "eel", "nightingale", "sparrow", "eagle", "pelican", "bullfrog", "anaconda", "iguana", "dingo", "caiman" "porpoise"]

word = random.choice(word_list)
word_display = "_" * len(word)
print(word_display)

input_list = ["Guess the letter.\n", "Can you guess the letter?\n", "Try to guess the letter.\n", "You Have To Guess the letter\n"]

input_list_two = ["You're almost there!\n", "The word is yet to be finished!\n"]

health = 5
filled = False
guessed_letters = []

while filled is False:
    if word_display.count("_") < 2:
        input_word = random.choice(input_list_two)
    else:
        input_word = random.choice(input_list)
    guess = input(input_word).lower()
    if guess in guessed_letters:
        print("You already guessed that letter. Please try again.\n")
        continue
    if guess not in word:
        health -= 1
        if health < 2:
            print(f"You have only {health} chance remaining!!! Considering yourself Chuck Norris, huh?")
        else:    
            print(f"The proposed letter is not in the word. You have {health} chances remaining.")
        if health == 0:
            print("\nGame over. See You Later Alligator!\n")
            print("""
⠀⠀   ⣠⣴⣾⣶⣿⣿⣶⣶⣶⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣼⣿⣿⣿⣋⣠⣿⣿⣿⣿⣿⡖⠀
⠀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿
⠀⠀⠻⣿⠟⠛⠛⠻⠟⠛⠋⢹⣿⣿⣿⢣
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⢇⣾⠀
⠀⠀⠀⠀⠀⢠⠀⠀⠀⢰⣤⣿⣿⢋
⠀⠀⠀⠀⠀⠻⠿⠿⠿⠿⣛
""")
            os.system('pause')
            break
    guessed_letters.append(guess)
    updated_word = letter_checker(word, guess, guessed_letters)
    print(updated_word)
    word_display = updated_word
    if "_" not in updated_word:
        filled = True

if filled:
    print("\nYou solved the word.\n")
    os.system('pause')