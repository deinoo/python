'''
Write a simple program that will execute a user-specified number of times. 
Each time the loop is started, it will ask for natural number and then display information:
- is the number a multiple of 3?
- is the number  a multiple of 4
- 'Yay' if the number is divided by both 3 and 4
- display an asterisk if none of the above conditions are met
'''

counter = int(input('How many times you would like to check number?: '))
for i in range (counter):
    a3 = a4 = a12 =0
    number=int(input('Enter number to check: '))
    if number % 3 ==0:
        print ('Number {} is divisible  by 3'.format(number))
        a3 = 1
    if number % 4 == 0:
        print('Number {} is divisible  by 4'.format(number))
        a4 = 1
    if a3 == a4 == 1:
        print('Yay! Number {} is divisible  by 12'.format(number))
        a12 = 1
    if a3 == 0 or a4 == 0 or a12 ==0:
        print ('*')
print ('We end here, we did {} checks for you'.format(counter))