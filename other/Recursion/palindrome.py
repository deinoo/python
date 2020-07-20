def palindrom (string):

    # # Iteration approach
    # listring = list(string)
    # for i in range(int((len(listring)+1)/2)):
    #     if listring[0]==listring[-1]:
    #         listring.pop(0)
    #         listring = listring[:-1]
    #     else:
    #         return 'its not a palindrome'
    # return f'{string} is palindrom'

    # Recursion approach
    n = len (string)
    listring = list(string)
    if n <= 2 and  listring[0]==listring[-1]:
        return 'its palindrome!'
    elif listring[0]==listring[-1]:
        return palindrom(listring[1:-1])
    else:
        return 'its not a palindrome'

string = 'rotoettotor'
print (palindrom(string))