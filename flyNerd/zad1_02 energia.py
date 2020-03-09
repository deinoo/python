plec = input('jestes (k)obieta czy (m)ezczyzna: ')
print (plec)
aktywnosc = input('Twoja aktywnosc to: \n-zero aktywnosci(a)\n-malo aktywnosci(b)\n-regularna aktywnosc(c)\n-duza aktywnosc(d)\n-extremanlna aktywnosc(e): ')
print (aktywnosc)
masa = float(input('podaj swoja wage: '))
print (masa)
wzrost= float(input('podaj swoj wzrost w cm: '))
print (wzrost)
wiek= float(input('Twoj wiek to: '))
print (wiek)


print(plec, aktywnosc, masa,wzrost,wiek)

def okresl(plec):
    if plec == 'k':
        wynik = -161
    elif plec == 'm':
        wynik = 5
    return wynik

def skala(aktywnosc):
    if aktywnosc == 'a':
        wynik = 1.2
    elif aktywnosc == 'b':
        wynik = 1.4
    elif aktywnosc == 'c':
        wynik = 1.6
    elif aktywnosc == 'd':
        wynik = 1.8
    elif aktywnosc == 'e':
        wynik = 2.0
    return wynik

print ('podstawowe zapotrzebowanie energetyczne to: ',float(10*masa+ 6.25*wzrost-5*wiek+ okresl(plec)))
print ('poszerzone zapotrzebowanie energetyczne to: ',(float(10*masa+ 6.25*wzrost-5*wiek+ okresl(plec))) *skala(aktywnosc))

