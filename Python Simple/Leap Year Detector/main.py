# Which year do you want to check?
year = float(input())
# 🚨 Don't change the code above 👆

# Check if the year is a leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            status = "Leap Year"
        else:
            status = "Not Leap Year"
    else:
        status = "Leap Year"
else:
    status = "Not Leap Year"

print(f"{status}")