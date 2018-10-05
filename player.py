class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.cards = []
        self.count = 0

    def updateState(self):
        self.count = 0
        for card in self.cards:
            try:
                cardVal = int(card.value)
            except ValueError:
                if(card == 'ace' and self.count > 11):
                    cardVal = 1
                else:
                    print('cardval11')
                    cardVal = 11
            self.count += cardVal
