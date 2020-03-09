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