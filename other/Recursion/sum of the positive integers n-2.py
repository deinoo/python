# Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-7.php

def sum_series(n):
    # # Classic approach
	# out = 0
    # for i in range(n+1):
    #     if not i%2:
    #         out += i
    # print (out)

    # # Recursion approach
    if n-2 <= 0:
        return n
    else:
        return n + sum_series(n-2)


print(sum_series(6)) #12
print(sum_series(13)) #49