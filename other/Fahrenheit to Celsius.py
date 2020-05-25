# fahrenheit to celsius with for loop and dict comprehension
def FahToCel():
    fa ={}
    fa ['t1'] = int(input('Provide temperature in Fahrenheit° to be converted to Celsius°: '))

    # for k,v in fa.items():
    #     fah [k] = round((v-32)*5/9,2)

    fah = {k:(round((v-32)*5/9,2)) for (k,v) in fa.items()}
    return ('Fahrenheit {}° is equal to {}° Celsius'.format (fa.get('t1'),fah.get('t1')))
print (FahToCel())