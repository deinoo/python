# Using the random module create another simple game.
# The computer draws a word from the available range (has a list of words).
# Then the letters are mixed. Mixed letters are shown to the player.
# The player must guess what the word is. The player guesses until the end.
# Only guessing stops the game.
# Extension: the player can select "q" or "Q" on the keyboard to end the game ahead of time.

import random

wordlist = ['foo', 'bar', 'doggy', 'catfish', 'female', 'train']

draw = random.choice(wordlist)
print(draw)
shuflelist = list(draw)
random.shuffle(shuflelist)
user = None

while user != draw:
    user = input('(press \'q\' or \'Q\' to quit) What word can you construct from{} letters?'.format(shuflelist))
    if user == "Q" or user =="q":
        print ('the end')
        break
    if user == draw:
        print('Bravo! Yours word: {} is matching drawed one: {}'.format(user, draw))