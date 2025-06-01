dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]

country_dial = {country: code for code, country in dial_codes}
print((country_dial))

lol = {code: country.upper() for country, code in sorted((country_dial).items()) if code < 70}

print(lol)

def dump(**kwargs):
    return kwargs

lol2 = dump(**{'x': 1}, y=2, **{'z': 3})
print(lol2)

# Объединение отображений оператором |
d1 = {'a': 1, 'b': 2}
d2 = {'a': 2, 'b': 6, 'c': 4}
print(d1 | d2)
