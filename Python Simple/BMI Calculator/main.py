# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = float(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = (weight / height ** 2)

if round(bmi, 2) < 18.5:
  status = "underweight"
elif round(bmi, 2) >= 18.5 and round(bmi, 2) < 25:
  status = "normal weight"
elif round(bmi, 2) >= 25 and round(bmi, 2) < 30:
  status = "slightly overweight"
elif round(bmi, 2) >= 30 and round(bmi, 2) < 35:
  status = "obese"
else:
  status = "clinically obese"

if status == "normal weight":
  print(f"Your BMI is {bmi}, you have a {status}.")
else:
  print(f"Your BMI is {bmi}, you are {status}.")