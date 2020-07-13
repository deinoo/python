# Write a Python program to calculate the harmonic sum of n-1.
# Note: The harmonic sum is the sum of reciprocals of the positive integers.
# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-8.php

def harmonicSum(n):
    # # Classic approach
    # out = 0
    # for i in range(1,n+1):
    #     out += 1/i
    #     print (out)
    # return out

    # # Generator approach
    # return sum(1/x for x in range(1,n+1))

    # # Recursion approach
    if n <= 1:
        return 1/n
    else:
        return 1/n + harmonicSum(n-1)

print(harmonicSum(13))