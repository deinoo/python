# Write a Python program to solve the Fibonacci sequence using recursion.
# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-5.php

def fibSeq(n):
    # # Classic approach
    # current = 1
    # prev = 1
    # result = 1
    # if n <= 2:
    #     return 1
    # for i in range (3,n+1):
    #     prev = current
    #     current = result
    #     result = current + prev
    # return  result

    # # Recursion approach
    if n < 2:
        return n
    else:
        return fibSeq(n-1) + fibSeq(n-2)

print(fibSeq(19))
