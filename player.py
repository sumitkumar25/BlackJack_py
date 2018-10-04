class Player:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.cards = []
        self.count = 0

    def updateState(self):
        self.count = len(self.cards)
