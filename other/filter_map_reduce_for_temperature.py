# Based on data show cities with positive temperature. Additionally - calculate average temperature for all cities.
# Use map(), filter() and reduce() function for that

from functools import  reduce

data_from_api = [
    {'city': 'Kraków', 'province_id': 8, 'current_temp': 3.5},
    {'city': 'Warszawa', 'province_id': 1, 'current_temp': 2.8},
    {'city': 'Suwałki', 'province_id': 9, 'current_temp': -0.5},
    {'city': 'Gdańsk', 'province_id': 3, 'current_temp': -0.1},
    {'city': 'Rzeszów', 'province_id': 7, 'current_temp': 3.9},
    {'city': 'Wrocław', 'province_id': 2, 'current_temp': 5.0},
]
#mapped = list(map(lambda cities:cities['city'], data_from_api))
#filtered = list (filter(lambda cities: cities ['current_temp']>=0, data_from_api))
mapped = list (map(lambda cities:cities['city'],filter(lambda cities: cities ['current_temp']>=0, data_from_api) ))
avg_temp = reduce((lambda avg, city: avg + city['current_temp']), data_from_api, 0) / len(data_from_api)

print (f"Cities with positive temperature: {', '.join(mapped)}")
print (f'Average temperature for all cities is: {avg_temp:.3}°C')