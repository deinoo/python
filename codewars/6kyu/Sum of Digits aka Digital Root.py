'''In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

Here's how it works:

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2'''

#solution without recurrency


def digital_root(n):
	valist = list(str(n))
	long = len(valist)
	sum1 = 0
	i1 = 0
	while i1 != int(long):
		sum1 = sum1 + int(valist[i1])
		i1 = i1 + 1

	long2 = len(str(sum1))
	sum2 = 0
	if long2 == 1:
		return sum1


	else :
		valist2 = list(str(sum1))
		i2 = 0
		while i2 != int(long2):
			sum2 = sum2 + int(valist2[i2])
			i2 = i2 + 1
		return sum2
