# kalkulator BMI https://www.flynerd.pl/2017/01/python-1-zabawy-w-konsoli.html

wzrost = input(str('podaj wzrost w cm:'))
waga = input(str('podaj wage:'))
wzrost = int(wzrost)/100
#print (wzrost)
bmi= int(waga)/wzrost**2
print (str(bmi))