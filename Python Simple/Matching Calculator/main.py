print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is your crush's name?
# 🚨 Don't change the code above 👆 
# Write your code below this line 👇
cname = name1 + name2
lname = cname.lower()

t = lname.count("t")
r = lname.count("r")
u = lname.count("u")
e = lname.count("e")
l = lname.count("l")
o = lname.count("o")
v = lname.count("v")

fd = str(t + r + u + e)

sd = str(l + o + v + e)

score = int(fd + sd)

if score < 10 or score > 90:
    print(f'Your Score is {score}, you go together like coke and mentos.')

if score >= 40 and score <= 50:
    print(f'Your Score is {score}, you are alright together.')

else:
    print(f'Your Score is {score}')