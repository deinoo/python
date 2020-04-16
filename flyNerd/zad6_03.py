# Save any three numbers.
# Find the largest number.
# Display numbers from largest to smallest.
# with conditional statements

no_of_lines = 3
lines = []
i=1
for i in range(no_of_lines):
    i+=1
    a=input('Input {} number please:'.format(i,))
    lines.append(int(a))

if lines[0] < lines[1]:
    if lines[1] < lines[2]:
        top = lines[2]
        second = lines[1]
        smallest = lines[0]
    else:
        top = str(lines[1])
        if  lines[0]< lines [2]:
            second = lines[2]
            smallest = lines[0]

elif lines[0]<lines[2]:
    top= lines[2]
    second = lines [0]
    smallest = lines [1]

else:
    top = lines[0]
    if lines[1] < lines [2]:
        second = lines [2]
        smallest = lines [1]
    else:
        second = lines [1]
        smallest = lines [2]

print ('Top number is: {}; it\'s {} number'.format(top,lines.index(int(top))+1))
print ('Sort desc is: {},{},{}'.format(top, second, smallest))