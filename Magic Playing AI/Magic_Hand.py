from statistics import mean
import random as rand



class Deck:

    def __init__(self):
        self.deck = []

    def deckgen(self):
        temp = 0
        #generate lands for the deck
        while len(self.deck) < 24:
            self.deck.append(temp)
        while len(self.deck) <60:
            temp = rand.randrange(0,20)
            self.deck.append(temp)
            #generate the core cards
        #shuffle the deck
        rand.shuffle(self.deck)
        #return the deck
        print(self.deck)
        return self.deck


class Hand():
    def __init__(self):
        self.hand = []


    def drawhand(self, mullt, deck):
        self.hand = []
        if mullt == 7:
            return self.hand, deck
        while len(self.hand) < (7 - mullt):
            self.hand.append(deck.pop())
        return self.hand, deck
  


    def handeval(self, hand):
        self.hand = hand
        x = 0
        lands = 0
        nonlands = 0 
        earlyp = 0 

        print(self.hand)
        while x < len(self.hand):  
            if self.hand[x] == 0:
                lands += 1
            elif self.hand[x] <= 3:
                nonlands += 1
                earlyp += 1
            else:
                nonlands += 1
            x += 1

        if ( 2 <= lands < 5 and earlyp >= 1):
            print ("hand is good")
            return True
        else:
            print ("hand is bad")
            return False


handc = Hand()
deckc = Deck()
deck = deckc.deckgen()
hand, deck = handc.drawhand(0,deck)
print (hand)
print (deck)
print (handc.handeval(hand))

mull = 0
while (handc.handeval(hand) == False) and (mull < 7):
    mull += 1
    hand, deck = handc.drawhand(mull, deck)

if handc.handeval(hand) == True:
    cardsinhand = 7 - mull
    print("your hand is good you have " + str(cardsinhand) + " cards in hand")
else:
    print("you never had a good hand go work on your deck")



