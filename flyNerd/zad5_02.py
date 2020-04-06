"""
Pobierz od użytkownika imię, nazwisko i numer telefonu,
a następnie:
    * Sprawdź czy imię i nazwisko składają się tylko z liter, a nr tel składa się wyłącznie z cyfr (wyświetl tę informację jako true/false)
    * Imię nazwisko popraw na pisane z dużej litery
    * Niektórzy podają numer telefonu z myślnikami lub z spacjami, usuń zbędne znaki z numeru
    * Sprawdź czy użytkownik jest kobietą
    * Połącz dane w jeden ciąg za pomocą spacji
    * Policz liczbę wszystkich znaków ww napisie
    * Podaj liczbę tylko liter w napisie
"""

name = input("Podaj imię: ")
surname = input('Podaj nazwisko: ')
phonenum = input('Podaj swoj nr telefonu: ')
sex = None

if name.isalpha() is True:
    name = name.capitalize()
    print('Twoje imię to {}!'.format(name))
else:
    print('Imię nie sklada sie z samych liter!')

if surname.isalpha() is True:
    surname = surname.capitalize()
    print('Twoje nazwisko to {}!'.format(surname))
else:
    print('Nazwisko nie sklada sie z samych liter!')

if phonenum.isdigit() is True:
    print('Twoj nr telefonu to: {}'.format(phonenum))
else:
    if phonenum.count('-') != 0:
        phonenum = phonenum.replace('-', '')
        print('Twoj numer telefonu to {}')
    elif phonenum.count('.') != 0:
        phonenum = phonenum.replace('.', '')
        print('Twoj numer telefonu to {}')
    elif phonenum.count(' ') != 0:
        phonenum = phonenum.replace(' ', '')
        print('Twoj numer telefonu to {}')
    else:
        print('Dziwne.. Twoj numer telefonu to {}.'.format(phonenum))

if name.rfind('a') == len(name) - 1:  # Specyfying  sex
    sex = 'K'
else:
    sex = 'M'

collect = (name, surname, phonenum)  # Creating personal string
personal = ' '.join(collect)
print(
    'Twoj identyfikator to {0}. Identyfikator liczy {1} znaków, i jest w nim {2} liter.'.format(personal,
                                                                                                              len(
                                                                                                                  personal),
                                                                                                              len(
                                                                                                                  personal) - personal.count(
                                                                                                                  ' ')-len(phonenum)))
