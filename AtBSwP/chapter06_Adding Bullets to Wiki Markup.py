""" Take a list from computer memory (copied there by Copy command):
"Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars"
and return it with extension of bulleting '* '
"""
import pyperclip

lista = pyperclip.paste().split('\r\n')
output = ''.join(['* '+ line + '\r\n' for line in lista])
pyperclip.copy(output)
# print ('Done')
