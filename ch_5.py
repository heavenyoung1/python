# Обзор построителей классов данных
import typing
from typing import NamedTuple
from collections import namedtuple

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