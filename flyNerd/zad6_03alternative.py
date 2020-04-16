# Save any three numbers.
# Find the largest number.
# Display numbers from largest to smallest.
# without conditional statements

no_of_lines = 3
lines = []
i=1
for i in range(no_of_lines):
    i+=1
    a=input('Input {} number please:'.format(i,))
    lines.append(int(a))

max_value = str(max(lines))
max_index= lines.index(int(max_value))+1
lines.sort(reverse=True)
print ('max_value:',type(max_value), max_value)
print ('Top number is: {}; it\'s {} provided number'.format(max_value,max_index))
print ('Sorted asc values are:',lines)