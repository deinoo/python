def collatz(number):

    if number %2 ==0:
        number //= 2
        print (number)
        collatz (number)
    elif number == 1:
        return number
    else:
        number = number* 3 +1
        print (number)
        collatz (number)