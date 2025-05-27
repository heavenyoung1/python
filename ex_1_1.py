import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])
ranks = []


class FrenchDeck():
    for i in range(2, 11):
        ranks.append(str(i))
    ranks += (list("JQKA"))
    print(ranks)

    suits = "spades diamonds clubs hearts".split()
    print(suits)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __str__(self):
        return f"Колода карт длиной {len(self)} включает в себя три первых карты {self._cards[:3]}"


deck = FrenchDeck()  # Создаём колоду
print(deck._cards)  # Выводим все карты

for card in deck:
    print(card)

print(deck[1:10])
print(deck)

# Рандомная карта из колоды
print(choice(deck))

# Проверка итерируемости класса
print(Card('Q', 'hearts') in deck)
print(Card('Q', 'lol') in deck)

suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

card1 = Card(rank='2', suit='clubs')
card2 = Card(rank='2', suit='diamonds')
card3 = Card(rank='2', suit='hearts')
card4 = Card(rank='2', suit='spades')

print(spades_high(card1))
print(spades_high(card2))
print(spades_high(card3))
print(spades_high(card4))

for card in sorted(deck, key=spades_high):
    print(card)

x = "ABC"
codes = [ord(i) for i in x]
print(codes)

codes1 = [last := ord(c) for c in x]
print(last)

# Сравнение спискового включения с map и filter
symbols = "!@#$%^&*()asfgjgkc,xnvg/"
beyond_ascii = [ord(s) for s in symbols if ord(s) > 100]
print(beyond_ascii)

beyond_ascii_1 = list(map(lambda c: c ** 2, map(ord, symbols)))
print((beyond_ascii_1))

def double(value):
    return value ** 2

s = [1, 2, 3, 4]
res = map(double, s)
print(list(res))

# Декартовы произведения

# Построение декартова произведения с помощью спискового включения
colors = ['black', 'white']

sizes = ['S', 'M', 'L']

t_shirts = [(color, size) for color in colors for size in sizes]
print(t_shirts)

for color in colors:
    for size in sizes:
        print(color, size)

aaa = tuple(ord(s) for s in symbols if ord(s) > 100)
print(aaa)

import array

array1 = array.array("I", (ord(symbol) for symbol in symbols))
print(array1)

# Порождение декартова произведения генераторным выражением
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)

# Кортежи как записи

#lax_coordinates = (33.945, -54.33)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [
    ('USA', '31195855'),
    ('BRA', 'CE342567'),
    ('ESP', 'XDA205856')
]

for passport in (traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

# Кортежи как неизменяемые списки
a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])
print(a != b)
b[-1].append(99)
print(a != b)
print(b)

def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

tf = (10, 'alpha', (1, 2)) # Здесь кортеж последний
tm = (10, 'alpha', [1, 2]) # Здесь список последний

print(fixed(tf))
print(fixed(tm))


lax_coordinates = (33.945, -54.33)
lat, long = lax_coordinates # Распаковка
print(f'latitude {lat}, longitude {long}')

divmod(20, 8)
print(divmod)
t = (20, 8)
print(divmod(*t))

a, b, *rest = range(5)
a, b, *rest = range(3)
a, b, *rest = range(2)
a, *body, c, d = range(5)

def fun(a, b, c, d, *rest):
    return a, b, c, d, rest

print(fun(*[1, 2], 3, *range(4, 10)))

print(*range(4), 4)
print([*range(4), 4])
print({*range(4), 4, *(5, 6, 7, 8)})

# Распаковка вложенных объектов

metro_areas = [
     ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
     ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
     ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
     ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
     ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name, _, _, (lat, lon) in metro_areas:
        if lon <= 0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

if __name__ == '__main__':
 main()