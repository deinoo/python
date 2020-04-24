# Write a script that calculates the factorial value. Solve the task with a for loop and while loop.

user = int(input('Provide number to calculate factorial value of it:'))
j=1
i=1

# FOR loop: 

for i in range (1,user+1):
    j=j*i

# WHILE loop:

# while i!=user+1:
#     j=j*i
#     i+=1

print ('{}! = {}'.format(user,j))