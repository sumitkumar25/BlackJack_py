import random
from card import Card


class Deck:
    suites = ['hearts', 'spade', 'diamond', 'clubs']
    value = list(range(2, 10))
    value.extend(['jack', 'queen', 'king', 'ace'])
    cards = []

    def __init__(self):
        for s in self.suites:
            for v in self.value:
                self.cards.append(Card(s, v, True))
        random.shuffle(self.cards)

    def getCard(self, hidden):
        randomCard = self.cards.pop()
        randomCard.hidden = hidden
        return randomCard
