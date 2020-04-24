# Write a program using a while loop, which for the next 10 natural numbers 
# will display the sum of its predecessors.
# Expected result: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

i=1
j=0
while i in range (1,11):
    j=j + i
    i +=1
    print (j)