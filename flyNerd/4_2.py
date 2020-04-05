# Utwórz spis oglądanych seriali.
# Każdy serial powinen mieć przypisaną ocenę w skali od 1-10.
# Zapytaj użytkownika jaki serial chce obejrzeć. W odpowiedzi podaj jego ocenę.
# Jesli brak w bazie podanego serialu - zapytaj użytkownika o dodanie kolejnego serialu i oceny.
# Dodaj nowy serial do spisu.
# wersja z elif

serials = {'Dead':5.2, 'Ray':7.2}
print ('co chcesz dzis obejrzec?', list(serials.keys()),': ', end='')
wybor = input()
if wybor in serials.keys():
    print ('swietny wybor, ocena {0} to {1}'.format(wybor, serials[wybor]))
else:
    ocena=input('podaj ocene dla {}: '.format(wybor))
    serials [wybor]= ocena

print ('w bazie mamy nastepujace seriale: ')
for i in serials: #print serials list with ranking
    print(i,':', serials[i])