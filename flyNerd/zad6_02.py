"""
Do kalkulatora BMI z lekcji "Python 1 zabawy w konsoli"
dodaj sprawdzanie czy BMI jest prawidłowe
Niedowaga       |   < 18,5
Waga normaln    |   18,5 – 24
Lekka nadwaga	|   24 – 26,5
Nadwaga	        |   > 26,5 - 30
Otyłość I stopnia   |	30 – 35
Otyłość II stopnia  |	30 – 40
Otyłość III stopnia |	> 40
"""

wzrost = input(str('podaj wzrost w cm:'))
waga = input(str('podaj wage:'))
wzrost = int(wzrost)/100
#print (wzrost)
bmi= int(waga)/wzrost**2

if bmi < 18.5:
    status = 'Niedowaga'
elif 18.5 < bmi < 24.5:
    status = 'Normalna waga'
elif 24.5 < bmi < 26.5:
    status = 'Lekka nadwaga'
elif 26.5 < bmi < 30:
    status = 'Nadwaga'
elif 30 < bmi < 35:
    status = 'Otylosc 1szego stopnia'
elif 35 < bmi < 40:
    status = 'Otylosc 2go stopnia'
elif 40 < bmi :
    status = 'Otylosci 3go stopnia'

print ('Twoje BMI to:', str(round(bmi,2)), 'co oznacza', status)