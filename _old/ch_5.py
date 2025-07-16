# Обзор построителей классов данных
import typing
from typing import NamedTuple
from collections import namedtuple
from dataclasses import dataclass

class Coordinate:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


moscow = Coordinate(55.76, 37.62)

Coordinate = typing.NamedTuple("Coordinate",
                               [('lat', float), ('lon', float)])

#Coordinate2 = typing.NamedTuple('Coordinate', lat=float, lon=float)

class Coordinate3(NamedTuple):
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat)}°{ns}, {abs(self.lon)}°{we}'

belgrad = Coordinate3(48.72, 94.56)

print(belgrad)

# Почему эта строка не работает
#print(f'IsSubClass {issubclass(Coordinate3, NamedTuple)}')

print(f'IsSubClass {issubclass(Coordinate3, tuple)}')

# Написание класса при помощи декоратора

@dataclass()
class CoordinateDataClass:
    lan: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.222, 95.444))

print(tokyo)
print(f'Tokey = Population {tokyo.population}, coordinates {tokyo.coordinates}')
print(City._fields)

delhi_data = ('Delhi NCR', 'IN', 21.395, Coordinate(53.444, 65.000))
delhi = City._make(delhi_data)
print(delhi)
print(delhi._asdict())
import json
print(json.dumps(delhi._asdict()))

Coordinate6 = namedtuple('Coordinate6', 'lat lon refrence', defaults=['WSG84'])
print(Coordinate6(0, 0))
print(Coordinate6._field_defaults)

class Coordinate7(NamedTuple):
    lat: float
    lon: float
    reference: str = "WSG84"







