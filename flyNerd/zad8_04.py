#Napisz skrypt obliczający wartość silnii. Rozwiąż zadanie za pomocą pętli for oraz pętli while. https://www.flynerd.pl/2019/06/python-8-petla-while.html


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
