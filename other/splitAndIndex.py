#LWe have a list of lists of words and we want to get a list of all the letters of these words
# along with the index of the list they belong to but only for words with more than two characters

strings = [ ['foo', 'bar'], ['baz', 'taz'], ['w', 'koko'] ]

def splitPlusIndex(value):
    # b = []
    # for lista in strings:
    #     for word in lista:
    #         if len(word)>2:
    #             for letter in word:
    #                 b.append((letter,strings.index(lista)))
    # print (b)
    return [(letter, strings.index(lista)) for lista in strings for word in lista if len(word)>2 for letter in word]

print (splitPlusIndex(strings))
