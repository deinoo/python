'''We can determine how many digits a positive integer has by
repeatedly dividing by 10 (without keeping the remainder) until the
number is less than 10, consisting of only 1 digit. We add 1 to this
value for each time we divided by 10.
Implement recursive algorithm in Python and test it using a
main function that calls this with the values 15, 105, and 15105.
http://www.cs.cmu.edu/~tcortina/activate/ct/lab8ques.pdf '''

def getBiggest (numbers):
	if len (numbers) <=1:
		return numbers[0]
	else:
		return max( numbers[0], getBiggest(numbers[1:]))


numbers = [2,3,6,9,1,23,6,3,2,6,7,9]
print (getBiggest(numbers))