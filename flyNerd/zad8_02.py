# Stwórz prostą grę zgadywankę. Komputer losuje wartość z przedziału od 1-30. Poproś użytkownika o zgadnięcie liczby. Program pyta użytkownika o podanie liczby tak długo, dopóki gracz nie zgadnie. https://www.flynerd.pl/2019/06/python-8-petla-while.html

import random
liczba = random.randint(0,30)
podane = ''
print ('zgadnij liczbe' + '('+str(liczba)+'):')
podane = input()
while liczba :
    if int(liczba) > int(podane):
        print ('podales za mala liczbe. Sprobuj ponownie')
        podane = input()
        continue
    elif int(liczba) < int(podane):
        print ('podales za duza liczbe. Sprobuj ponownie')
        podane = input()
        continue
    elif int(liczba) == int(podane):
        print('brawo')
        break

# pomyslec o:
# import random
# 
# a = random.randint(1,30)
# #guess = int(input("Zgadnij liczbę w zakresie od 1 do 30"))
# 
# while True:
#     guess = int(input(str(a)+" Zgadnij liczbę w zakresie od 1 do 30: "))
#     if a == guess:
#         print("Brawo, to ta liczba!")
#         break
#     else:
#         print("Niestety, próbuj dalej")
#         if guess > a:
#             print("Twoja liczba jest większa")
#         else:
#             print("Twoja liczba jest mniejsza")
#             continue
# print ('rozwiazane!')