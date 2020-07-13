# Write a Python program to get the factorial of a non-negative integer.
# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-4.php

def factorial(n):
    # Classic approach
    # i=1
    # out = 1
    # while i <= n:
    #     out *= i
    #     i+=1
    # return  out

    # Recursion approach
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


print(factorial(1))
