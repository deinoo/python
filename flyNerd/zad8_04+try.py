# Write a script that calculates the factorial value. Solve the task with a for loop and while loop.
# with error handling
def fac(user):
    if isinstance(user,(int,float)):
        if user < 0:
            print('(reason:negative)Positive number please')
            return None
        try:
            j = 1
            i = 1
            for i in range(1, user + 1):
                j = j * i
            print('{}! = {}'.format(user, j))
        except (ValueError,TypeError,NameError) as e:
            print('Digit please, bro, or we\'re done with',e)
            print('Nothing to print for {}!, sorry'.format(user))
            return e
        return j
    else:
        print('(reason:non_int)Natural number please')

fac ('w')

