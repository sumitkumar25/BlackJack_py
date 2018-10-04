from player import Player
from deck import Deck


class BlackJack:
    def initGame(self):
        print("welcome to backjack")
        self.p = Player(input("please enter your name "), 1)
        self.d = Player('Dealer', 2)
        self.deck = Deck()
        self.dealInitialHand()
        self.displayCards()
        self.dealHand()

    def dealInitialHand(self):
        self.p.cards.append(self.deck.getCard(False))
        self.d.cards.append(self.deck.getCard(False))
        self.p.cards.append(self.deck.getCard(False))
        self.d.cards.append(self.deck.getCard(True))

    def displayCards(self):
        for gamePlayer in [self.p, self.d]:
            print(gamePlayer.name + '  has: ')
            for c in gamePlayer.cards:
                if(not c.hidden):
                    print('    '+str(c.value) + ' of ' + c.suite)
                else:
                    print("    hidden Card")

    def dealHand(self):
        self.p.updateState()
        self.d.updateState()
        while(self.p.count < 21 and self.d.count < 21):
            if(len(self.p.cards) >= len(self.d.cards)):
                playerAction = input(self.p.name + 'Hit or Miss')
                if(playerAction.lower() == 'hit'):
                    self.p.cards.append(self.deck.getCard(True))
                elif(playerAction.lower() == 'miss'):
                    pass
                else:
                    continue
            else:
                self.p.cards.append(self.deck.getCard(True))



game=BlackJack()
game.initGame()
