print("We only have about 4000 weeks in our life depending on how we manage our health.")
print("This simple Calculator may tell how many weeks do we have left.")
age = input("Enter Your Age: ")

age = float(age)
week = 90 *52
rw = round(week - (age*52))

print(f"You may only have {rw} week left.")
print("Result is experimental")
