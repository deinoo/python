'''You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)'''

def find_outlier(integers):
    evencnt = oddcnt = 0
    for n in integers:
        if n%2 == 0: evencnt +=1
        elif n % 2 != 0: oddcnt += 1
        if evencnt > 1:
            for m in integers:
                if m % 2 != 0:
                    return m
        if oddcnt > 1:
            for m in integers:
                if m % 2 == 0:
                    return m