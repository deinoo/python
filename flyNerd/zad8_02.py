# Create a simple guessing game. The computer randomizes a value between 1-30. 
# Ask the user to guess the number. 
# The program asks the user to enter the number until the player guesses.

import random
x = random.randint(0,30)
print(x)
user = None
while x != user:
    user=int(input('Let\'s guess a number from range (0,30):'))
    continue
print ('Bravo, number is',x)