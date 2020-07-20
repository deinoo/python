# exponentiation

def power(base, pow):
	if pow == 1:
		return base
	else:
		return base * power(base,(pow-1))
		
	# if pow == 0:
		# return 1
	# else:
		# return base * power(base,(pow-1))		

print (power(2,16))