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

deck = FrenchDeck()  # Создаём колоду
print(deck._cards)   # Выводим все карты