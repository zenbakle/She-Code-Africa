import random
# Generate Number
x = random.randint(0,20)
# Ask for a guess
b = input("Guess a number between 0 and 20\n")
# Make sure number is in range
if int(b) not in range(0,21):
    print("Number is out of range")
else:
    if int(b) < x: # check if number is low
        print("Number too low")
    elif int(b) > x: # Check if number id high
        print("Number too high")
    else:
        print("Correct guess") # Good guess message