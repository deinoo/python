'''Write a Python program of recursion list sum.
https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
'''

def recursive_list_sum(data_list):
    summ = 0
    for item in data_list:
        if isinstance(item,int):
            summ += item
        else:
            summ += recursive_list_sum(item)
    return summ




print( recursive_list_sum([1, 2, [[[3,4],[[4,4],[4,3]]]],[5,6]]))