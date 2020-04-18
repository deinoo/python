# Write a program that will display their value up to the cube for 10 consecutive natural numbers.

number= int(input('Provide 1st number to be up to the cube for next 10 consecutive natural number: '))
for i in range (number,number+10):
    print (i,': ', i**3)