# Given an array, find the integer that appears an odd number of times.
#
# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    return [num for num in set(seq) if seq.count(num)%2 != 0][0]