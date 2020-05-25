'''Write a method that takes a sequence of objects with two keys each: country or state, and capital. Keys may be symbols or strings

The method should return an array of sentences declaring the state or country and its capital.

Examples

[{"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital" : "Madrid"}] --> ["The capital of Maine is Augusta", "The capital of Spain is Madrid"]'''

def capital(capitals):
    return  [(f"The capital of {dicti['state']} is {dicti['capital']}") if 'state' in dicti else (f"The capital of {dicti['country']} is {dicti['capital']}") for dicti in capitals]