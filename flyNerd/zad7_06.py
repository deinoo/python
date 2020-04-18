# Display the classic multiplication table in the console

for i in range (1,11):
    if i == 1:
        print('-' * 17)
    for j in range (1,11):
        print('||{:2} * {:2} ={:3} ||'.format(i,j,i*j))
        if j==10:
            print('='*17)