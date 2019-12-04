'''
This class represents a playing card. It will contain a number and a suit.

Aggie Wheeler Bateman
12/4/19
'''

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = 0

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank

    def setValue(self):
        if self.rank > 10:
            self.value = 10
        else:
            self.value = self.rank
        return self.value

    def getSuit(self):
        self.s = ""
        if self.suit == 'd':
            self.s = 'diamonds'
        elif self.suit = 'h':
            self.s = 'hearts'
        elif self.suit = 'c':
            self.s = 'clubs'
        else:
            self.s = 'spades'
        return self.s

    def __str__(self):
        if self.rank > 1 and self.rank < 11:
            self.name = str(self.rank) + " of " + self.getSuit()
        if self.rank == 1:
            self.name = "The Ace of " + self.getSuit()
        if self.rank == 11:
            self.name = "The Jack of " + self.getSuit()
        if self.rank == 12:
            self.name = "The Queen of " + self.getSuit()
        if self.rank == 13:
            self.name = "The King of " + self.getSuit()
            return self.name
            
