from random import randint

NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
COLORS = ["🔴","🟢","🟡","🔵"]


class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def ___str___(self):
        return f"{self.color} {self.number}"   


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def __str__(self):
        return f'{self.name}'
        


class Deck:
    def __init__(self, numbers, colors):
        self.cards = []
        for number in numbers:
            for color in colors:
                card = (color, number)
                self.cards.append(card)

    def shuffle(self):
        shuffled_deck = []
        deck_to_shuffle = self.cards.copy()
        while len(deck_to_shuffle) > 0:
            card_to_move = deck_to_shuffle[randint(0, len(deck_to_shuffle)-1)]
            deck_to_shuffle.remove(card_to_move)
            shuffled_deck.append(card_to_move)
        return shuffled_deck


class Game:
    def __init__(self):
        # make sure to pay attention to caps when using attributes
        # self.deck = Deck (capital letter)establishes the deck 
        # calling .shuffle at end the line of code will shuffle the cards 
        self.deck = Deck(NUMBERS, COLORS).shuffle()
        self.player1 = Player("Joe")
        self.player2 = Player("Mary")
    # this is used to print every card in the deck 
        for card in self.deck: 
            print(card)
        print(self.player1, self.player2)
    
    # pop will append one card from 
    def deal_cards(self):
        for i in range(7):
           self.player1.hand.append(self.deck.pop())
           self.player2.hand.append(self.deck.pop())
        print(len(self.player1.hand), len(self.player2.hand))

# Player1 takes turn 
#   Game starts here 
game = Game()
deck = game.deck
game.deal_cards()

