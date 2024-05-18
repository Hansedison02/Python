import random
import os

r = "rock"
p = "paper"
s = "scissors"
answer2 = ""
answer = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if answer == "0":
    answer2 = r
elif answer == "1":
    answer2 = p
elif answer == "2":
    answer2 = s

if answer2 not in [r, p, s]:
    print("Invalid answer")
else:
    print(f"You choose: {answer2}")
    c_choice = random.choice([r, p, s])
    print(f"COM choose: {c_choice}")
    if answer2 == s and c_choice == r:
        print("You Lose")
    elif answer2 == s and c_choice == p:
        print("You Win")
    elif answer2 == p and c_choice == s:
        print("You Lose")
    elif answer2 == p and c_choice == r:
        print("You Win")
    elif answer2 == r and c_choice == p:
        print("You Lose")
    elif answer2 == r and c_choice == s:
        print("You Win")
    elif answer2 == c_choice:
        print("Draw")
    else:
        print("TBD")

os.system('pause')
