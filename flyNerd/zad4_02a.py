# Utwórz spis oglądanych seriali.
# Każdy serial powinen mieć przypisaną ocenę w skali od 1-10.
# Zapytaj użytkownika jaki serial chce obejrzeć. W odpowiedzi podaj jego ocenę.
# Jesli brak w bazie podanego serialu - zapytaj użytkownika o dodanie kolejnego serialu i oceny.
# Dodaj nowy serial do spisu.
# wersja z funkcjami

serialss = {'Casa': 8, 'Dead': 7, 'Suits': 5}
wybor = None
def spytaj():
    print('Co dzis ogladamy? ', list(serialss.keys()), 'wybierz podajac tytul: ', end='')
    wybor = input()
    return wybor
def zdecyduj():
    if wybor in serialss:
        print('super! Ocena {}  to : {} '.format(wybor, serialss[wybor]))
    else:
        print('o, nie gramy tego. Dodaje do bazy. Podaj ocene dla tego serialu: ', end='')
        ocena = input()
        serialss[wybor] = ocena
wybor = spytaj()
zdecyduj()

print('Aktualna lista pozycji to: ', list(serialss))