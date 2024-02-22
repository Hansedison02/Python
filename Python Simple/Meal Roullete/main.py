names_string = "Akira, Akari, Akiro"

names = names_string.split(", ")

import random

l = len(names)

puppet = random.randint(0, l - 1)

print(f"{names[puppet]} is going to buy the meal today!")