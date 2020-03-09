print ('podaj liczbe calkowita do 15')
n = int(input())
i=1
j=1 #suma silni
for i in range (n):
    i=i+1
    j=j*i
    #print (j)
print (str(n)+'! = ' + str(j))

print ('podaj liczbe calkowita do 15')
n = int(input())
i=1
j=1 #suma silni
while i !=n:
    i=i+1
    j=j*i
   #print (j)
print (str(n)+'! = ' + str(j))


def silnia(wart):
    i = 1
    j = 1  # suma silni
    while i != wart:
        i = i + 1
        j = j * i
        #print(j)
    print(str(wart) + '! = ' + str(j))
silnia(6)