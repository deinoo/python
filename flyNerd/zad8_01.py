# Napisz program z wykorzystaniem pętli while, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
# Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55 
# https://www.flynerd.pl/2019/06/python-8-petla-while.html

j = 0  # suma liczb
skok = 0 #ile liczb dodac
iss = 0 #wartosc poczatkowa
print ('podaj od jakiej liczby zaczynamy')
i= input() #i - liczba od ktorej startujemy odliczanie
iss=int(i) # i startowe def
print('ile cyfr kolejnych wziasc?')
skok = input()

i=int(i)
skok= int(skok)

while i != iss +skok:
    j=j+ int(i)
    print (j)
    i=i+1

# j = 0  # suma liczb
# skok = 0 #ile liczb dodac
# print ('podaj od jakiej liczby zaczynamy')
# i= input()
# print('ile cyfr kolejnych wziasc?')
# skok = input()
# i=int(i)
# skok= int(skok)
# for k in range (skok):
#     j=j+ int(i)
#     print (j)
#     i=i+1