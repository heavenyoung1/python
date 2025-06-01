
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
#print(d1 |= d2) Вот эта хрень не работает

# Сопоставление с объектом - образцом

from collections import OrderedDict

def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f'Invalid "book" record: {record!r}')
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')


b1 = dict(api=1, author='Douglas Hofstadter', type='book', title='Gödel, Escher, Bach')
b2 = OrderedDict(api=2, type='book', title='Python in a Nutshell', authors='Martelli Ravenscroft Holden'.split())

print(get_creators(b1))
print(get_creators(b2))

# Проверка шэширумости

tt = (1, 2, (3, 4))
print(hash(tt))

tl = (1, 2, [3, 4])
#hash(tl) 