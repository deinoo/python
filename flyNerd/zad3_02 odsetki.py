# Napisz skrypt, który, który obliczy stan konta za kilka lat z uwzlednieniem kapitalizaji miesiecznej https://www.flynerd.pl/2017/01/python-3-formatowanie-napisow.html

stan = int(input('podaj aktualny stan konta: '))
oprocentowanie = float(input('jakie jest oprocentowanie lokaty: '))
czas = int(input('ile lat bedzie trwala lokata: '))
oprocentowaniem = oprocentowanie / 12
czasm = czas * 12

def odsetki(stan):
    for mc in range(czasm):
        stan = stan + (oprocentowaniem * stan)/100
        mc += mc
    return stan
print (odsetki(stan))
print ('Twoj stan poczatkowy {} przez {} lat czyli {} m-cy przy oprocentowaniu {} urosnie do {:.2f} pln!'.format(stan,czas, czasm,oprocentowanie, odsetki(stan)))
