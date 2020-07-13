# Write a Python program to calculate the value of 'a' to the power 'b'.
# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-10.php

def expo (base,power):
    # # Classic approach
    # out = 1
    # for i in range (1, power+1):
    #     out *= base
    # return out

    # # Recursion approach
    if power <= 0:
        return 1
    else:
        return base * expo(base,power-1)

print(expo(2,4))