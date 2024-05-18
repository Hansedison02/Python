target = int(input()) # Enter a number between 0 and 1000
if target > 1000:
    print("Invalid Number")
else:
    total = 0

    for n in range(2, target+1, 2):
        total += n

    print(total)