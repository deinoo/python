"""A friend of mine takes a sequence of numbers from 1 to n (where n > 0).
Within that sequence, he chooses two numbers, a and b.
He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.
Given a number n, could you tell me the numbers he excluded from the sequence?
The function takes the parameter: n (n is always strictly greater than 0) and returns an array or a string (depending on the language) of the form:

[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]
with all (a, b) which are the possible removed numbers in the sequence 1 to n.

[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or ...will be sorted in increasing order of the "a".

It happens that there are several possible (a, b). The function returns an empty array (or an empty string) if no possible numbers are found which will prove that my friend has not told the truth! (Go: in this case return nil).

(See examples of returns for each language in "RUN SAMPLE TESTS")

Examples:
removNb(26) should return [(15, 21), (21, 15)]
"""

#'''bruteforce approach'''
# def removNvalue(n):
# 	lista = list(range(1,n+1))
# 	out = []
# 	add = sum(lista)
# 	for first in lista:
# 		for second in lista:
# 			if first * second == add - first - second:
# 				out.append((first,second))
#
#'''list comprehension solution (bruteforce)'''
# def removNB(n):
# 	lista = list(range(1,n+1))
# 	out = []
# 	add = sum(lista)
# 	out = [(first, second) for first in lista for second in lista if first * second == add - first - second]
# 	print (out)
# 	return out

def removNB(n):
	#print (n)
	add = int(n* (n+1)/2)
	out = []
	for value in range (0,n+1) :
		a = ((add - value) / (value+1))
		if a.is_integer() and a<n:
			out.append ((int(a),int(value)))
	#print (out)
	return out


n = 1000008 # 26,101, 325,1000008
print (removNB(n))