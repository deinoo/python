"""Write a Pig LatinIf function which translate sentence to a Pig Latin language. The rules are simple: if word begins with a vowel, the word yay is added to the end of it. If a word begins with a consonant or consonant cluster (like ch or gr), that consonant or cluster is moved to the end of the word followed by ay."""

def pigLatin(sentence):
    lista = message.split()
    output = []

    def vowel(check):  # function handling words starting with vovels
        if check[0].islower():
            output.append(check + 'yay')
        else:
            output.append(check + 'YAY')

    def nonalphanum(check):  # function handling words starting with non-alpha-numeric char
        output.append(check)

    def consonant(check):  # function handling words starting with consonant
        for char in check:
            if char.lower() in ('a', 'e', 'i', 'o', 'u', 'y'):
                before, sep, after = check.partition(
                    check[:(check.find(char))])  # partition slice on chars without vovels
                if check.islower():
                    return output.append(after + sep[::-1] + 'ay')
                elif check.istitle():
                    return output.append(after[0].upper() + sep[::-1].lower() + 'ay')
                elif check.isupper():
                    return output.append(after + sep[::-1] + 'AY')
                else:
                    return 'You miss some condition dude ;)'

    prefixNonAlnum = ''  # definition of non-alpha-numeric prefix
    suffixNonAlnum = ''  # definition of non-alpha-numeric suffix
    if not lista[0][0].isalnum() and len(lista[0]) > 0:  # condition and action for non=alpha-numeric prefix
        prefixNonAlnum = lista[0]
    if not lista[-1][-1].isalnum() and len(lista[-1]) > 0:  # condition and action for non=alpha-numeric suffix
        suffixNonAlnum = lista[-1][-1]
        lista[-1] = lista[-1][:-1]

    for items in lista:  # action conditions for words
        if items[0].lower() in ('a', 'e', 'i', 'o', 'u', 'y'):
            vowel(items)
        elif items[0].isalpha():
            consonant(items)
        elif items[0].isnumeric():
            nonalphanum(items)
        else:
            nonalphanum(items)

    return prefixNonAlnum + ' '.join(output) + suffixNonAlnum


message = 'My name is BARTOSZ BUDZIK and I am 9,999 years old.'
print(pigLatin(message))