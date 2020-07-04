# Recursion: Sum of a list of numbers
# Write a Python program to calculate the sum of a list of numbers.
# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
# desc version
def sum_num(list):
    if len(list) <=1:
        return list[0]
    else:
        return list[len(list)-1] + sum_num(list[:len(list)-1])


#num = [3]
num = [2,3,4,5,6,7]
print (sum_num(num))


# asc version
# def sum_num(list):
#     if len(list) <=1:
#         return list[0]
#     else:
#         return list[0] + sum_num(list[1:])
# 
# 
# #num = [3]
# num = [2,3,4,5,6,7]
# print (sum_num(num))
