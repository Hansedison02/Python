import random

print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢀⣀⣀⣀⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⣼⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⢰⣿⣿⣿⣿⣿⡇⠀⠀⠀
⢠⣤⣤⣤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⢸⣿⣿⣿⣿⡿⠀⠀⠀⠀
⠘⢿⣿⣷⣶⣦⣬⣍⡛⠒⢦⣄⠀⠀⠀⠀⢀⣤⣄⣼⣧⢸⣿⣿⣿⣿⠃⠀⠀⠀⠀
⠀⠀⠻⣿⣿⣿⣿⣿⣿⣷⣄⡈⠳⣄⡴⡿⠉⠘⠁⠀⠛⠉⠻⣿⡿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⡿⠆⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠙⠿⠿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⢻⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡄⠀⠤⢦⠀⠀⠀⠀⠀⣿⣿⣷⢀⡸⠧⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠸⣶⣾⡄⠀⠀⠀⠀⠹⣻⡫⣏⠆⠀⣜⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠫⠿⠃⢤⣬⠧⢴⠀⠀⣠⡿⢋⣻⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣿⣦⣄⠀⠀⠀⠣⣀⣜⣤⣾⡿⠁⠀⠀⡿⢣⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠁⠀⠀⠀⠈⣻⠛⠛⠿⠛⠛⠛⠉⢣⠀⠀⣰⠇⡈⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣴⣶⠲⣶⣶⣟⡀⠀⠀⠀⠀⡈⠀⡆⢹⣿⡏⠠⣦⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣼⢄⠈⠉⣇⢀⠀⠀⠀⠘⠀⣇⣼⣿⣷⠞⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡉⠛⣷⣠⣾⠿⣶⣇⠀⣆⣾⣿⣿⣿⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡯⢣⡈⢙⢾⠉⠀⠀⠑⣜⣿⣷⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣯⣉⡆⠑⣧⡀⠀⠀⠀⠙⠛⠛⠉⠉⠙⢿⣿⣿⣷⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣶⣴⣾⣷⣤⣶⣾⣷⣦⠀⠀⠀⠀⠀⣿⣿⣿⣿⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⢿⣿⣿⣿⣿⣦⡀⠀⠀⡰⢡⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠛⠋⠛⢿⣿⣥⣭⣶⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠝⣦⠤⠀⣿⣿⣿⣿⣿⢿⣿⣿⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⢒⠟⠛⢻⣿⠁⣰⡿⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠈⠂⠒⠒⠛⠛⠋⠀⠀⠀
      ''')
# Letters (uppercase and lowercase)
letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']

# Numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Symbols
symbols = ['^', '*', '#', '!', '?', '~',':', ';']

print("EEVEE PWD GENERATOR")
nr_letters = int(input("How many letters?\n"))
nr_numbers = int(input("How many numbers?\n"))
nr_symbols = int(input("How many symbols?\n"))

password = []

# Generate letters
for _ in range(nr_letters):
    password += random.choice(letters)

# Generate numbers
for _ in range(nr_numbers):
    password += random.choice(numbers)

# Generate symbols
for _ in range(nr_symbols):
    password += random.choice(symbols)

# Shuffle the password
random.shuffle(password)

pwd = ""

for ch in password:
    pwd += ch

print("Your password is:", pwd)
