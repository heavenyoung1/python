import collections

Card = collections.namedtuple("Card", ["rank", "suit"])
ranks = []

class FrenchDeck():
    for i in range(2, 11):
        ranks.append(str(i))
    ranks += (list("JQKA"))
    print(ranks)
