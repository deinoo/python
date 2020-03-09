# konwerter jednostek https://www.flynerd.pl/2017/01/python-3-formatowanie-napisow.html

wartosc = input('podaj dlugosc w centymetrach:')
wartoscm = int(wartosc)/100
wartoscc = round(int(wartosc)/0.39370079,2)

print('{}cm to inaczej {} metrow albo {} cali '.format(wartosc,wartoscm, wartoscc))