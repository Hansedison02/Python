print("Tip Calculator")
bill = input("How much is the total bill?\n$")
tip = input("How much in percent are you willing to give the tip?\n")
people = input("How many person attended the social event?\n")

bill = float(bill)
tip = float(tip)
people = float(people)

tip = bill * (tip/100)

price = round((bill + tip)/people, 2) 

print(f"Each person should spend: ${price}")