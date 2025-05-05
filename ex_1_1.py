import collections

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


deck = FrenchDeck()  # Создаём колоду
print(deck._cards)  # Выводим все карты

for card in deck:
    print(card)

print(deck[1:10])
