from player import Player
from deck import Deck


class BlackJack:
    def initGame(self):
        print("welcome to backjack")
        self.p = Player(input("please enter your name "), 1)
        self.d = Player('Dealer', 2)
        self.deck = Deck()
        self.dealInitialHand()
        self.gameEnd = False
        self.displayCards()
        self.dealHand()

    def dealInitialHand(self):
        self.p.cards.append(self.deck.getCard(False))
        self.d.cards.append(self.deck.getCard(False))
        self.p.cards.append(self.deck.getCard(False))
        self.d.cards.append(self.deck.getCard(False))
        self.p.updateState()
        self.d.updateState()

    def displayCards(self):
        for gamePlayer in [self.p, self.d]:
            print(gamePlayer.name + '  has: total ' + str(gamePlayer.count))
            for c in gamePlayer.cards:
                if(not c.hidden):
                    print('    '+str(c.value) + ' of ' + c.suite)
                else:
                    print("    hidden Card")

    def dealPlayer(self):
        playerAction = input(self.p.name + ' Hit or Miss ')
        if(playerAction.lower() == 'hit'):
            self.p.cards.append(self.deck.getCard(False))
            self.p.updateState()
        elif(playerAction.lower() == 'miss'):
            pass
        else:
            print('invalid input please retry')
            self.dealPlayer()
        self.displayCards()


    def dealDealer(self):
        self.d.cards.append(self.deck.getCard(False))
        self.d.updateState()
        print('dealer dealt')
        self.displayCards()

    def checkGame(self):
        pc = self.p.count
        pd = self.d.count
        winner = None
        loser = None
        if(pc > 21 and pd <= 21):
            self.gameEnd = True
            loser = self.p
            winner = self.d
        elif(pd > 21 and pc <= 21):
            self.gameEnd = True
            loser = self.d
            winner = self.p

        if(self.gameEnd):
            print('winner is {0} with score {1} and loser is {2} with score {3}'.format(
                winner.name, winner.count, loser.name, loser.count))

    def dealHand(self):
        while(not self.gameEnd):
            self.dealPlayer()
            self.checkGame()
            self.dealDealer()
            self.checkGame()


game = BlackJack()
game.initGame()
