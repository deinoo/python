# Fibonacci series calculation

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 0:
        return 0
    # Second Fibonacci number is 1
    elif n == 1:
        return 1
    else:
        series = [0, 1]
        for i in range(1, n):
            series.append(series[i]+series[i-1])
#            print ('i:', series[i], 'i-1:', series[i-1], 'suma:',(series[i]+series[i-1]))
        return (series[n])

value = int(input('Provide number for Fibonacci series calculation:'))
print('For n={} Fibonacci series is {}'.format(value, Fibonacci(value)))

