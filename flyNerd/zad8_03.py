# Create a simple guessing game. The computer randomizes a value between 1-30. 
# Ask the user to guess the number. 
# The program asks the user to enter the number until the player guesses.
# Player should receive information whether provided number is too big or too small.

import random
x = random.randint(0,30)
print(x)
user = None
while x != user:
    user=int(input('Let\'s guess a number from range (0,30):'))
    while x < user:
        print('Your number is bigger than the one we\'re searching for')
        break
    while  x > user:
        print('Your number is smaller than the one we\'re searching for')
        break
    continue
print ('Bravo, number is',x)