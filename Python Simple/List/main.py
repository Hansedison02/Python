line1 = ["⬜️","️⬜️","️⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️","️⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️","️⬜️","️⬜️"]
line4 = ["⬜️","️⬜️","️⬜️","️⬜️","️⬜️"]
line5 = ["⬜️","⬜️","️⬜️","️⬜️","️⬜️"]
map = [line1, line2, line3, line4, line5]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

letter = position[0].capitalize()

index = ["A", "B", "C", "D", "E"]

l_position = index.index(letter)
n_position = int(position[1]) -1

map[l_position][n_position] = "X"

print(f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}")