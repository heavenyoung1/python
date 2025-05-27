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


