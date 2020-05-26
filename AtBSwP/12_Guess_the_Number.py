# guess the correct number using the hint for the answer range. Prevent errors

import random

name = input('Whats ur name? ')
attempts  = int(input('How many time you want to try?: '))
print ('Hi {}, guess a number im thining about. '.format(name))
secretNumber = random.randint(1,20)

for guessesTaken in range (1,attempts+1):
    guess = input('Take a guess: ')
    try:
        guess = int(guess)
        if guess == secretNumber:
            break
        elif guess > secretNumber:
            print('Your number is too high')
        elif guess < secretNumber:
            print('Your number is too low')
    except (ValueError)as e:
        print('we can\'t match {} with secret number. Use natural number'.format(guess))

if guess == secretNumber:
    print ('You find my number:{} in {} attempts'.format(secretNumber,guessesTaken))
else:
    print('You didnt guess my number:{} in {} guesses'.format(secretNumber, guessesTaken))
