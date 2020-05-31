'''Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.'''

spam = ['a','b',2,3,'r']

def addAnd(lista):
    out = ''.join(['and ' + str(items) if lista.index(items) == len(lista)-1 else str(items) + ',' for items in lista])
    return out
print (addAnd(spam))
