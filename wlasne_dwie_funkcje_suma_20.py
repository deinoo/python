def pobierz_wynik():
    podana=int(input('podaj wynik dzialania 5+15: '))
    return podana

def porownaj(podana):
    oczekiwana = 20
    return podana == oczekiwana


podana = pobierz_wynik()
print (podana)

while not porownaj(podana):
    print('no chyba jednak nie do konca..', end='')
    podana = pobierz_wynik()
print ('brawo')

