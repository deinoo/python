''' Return an array containing the numbers from 1 to N, where N is the parametered value. N will never be less than 1.

Replace certain values however if any of the following conditions are met:

If the value is a multiple of 3: use the value 'Fizz' instead
If the value is a multiple of 5: use the value 'Buzz' instead
If the value is a multiple of 3 & 5: use the value 'FizzBuzz' instead'''

def fizzbuzz(n):
    return [
        'FizzBuzz' if value % 15 == False else 'Fizz' if value % 3 == False else 'Buzz' if value % 5 == False else value for value in list(range(0,n+1))]


print (fizzbuzz(15))
