# Write a Python program to get the sum of a non-negative integers in number.
# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-6.php

def sumDig(n):
    # # Classic approach
    #return sum(int(item) for item in str(n))

    # # Classic FOR LOOP approach
    # out = 0
    # for item in str(n):
    #     out += int(item)
    # return out

    # # Recursion approach
    n = str(n)
    if len(str(n)) <= 1:
        return int(n)
    else:
        return int(n[:1]) + sumDig(int(n[1:]))

#print(sumDig(345))
print(sumDig(345132))
