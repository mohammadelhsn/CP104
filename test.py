
airport_codes = {
    'Washington': 'IAD',
    'Tokyo': 'NRT',
    'Paris': 'CDG',
    'Amsterdam': 'AMS',
    'Minneapolis': 'MSP'
}

new_airport_codes = {
    'Tokyo': 'HND',
    'San Jose': 'SJC',
    'Los Angeles': 'LAX'
}

print(airport_codes.get('Los Angeles', 'na'))
print(airport_codes.get('Tokyo', 'na'))
airport_codes.update(new_airport_codes)
print(airport_codes.get('Los Angeles', 'na'))
print(airport_codes.get('Tokyo', 'na'))
