from random import randint

# 2 spaces before a class 
# 1 spaces before a method 
# exit() to get out of PYTHON shell
#add, commit, push
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
COLORS = ["🔴","🟢","🟡","🔵" ]
# SPACE
# SPACE
class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def ___str___(self):
        return f"{self.color} {self.number}"   
# SPACE
# SPACE
class Player:
    def __init__(self, name):
        self.name = name 
        self.hand = []
# SPACE
# SPACE
class Deck:
    def __init__(self, numbers, colors):
        self.cards = []
        for number in numbers:
            for color in colors:
                card = (color, number)
                self.cards.append(card)

    def shuffle(self):
        shuffle_deck = []    
        deck_to_shuffle = self.cards.copy()
        while len(deck_to_shuffle) > 0:
            # pull random card from unshuffled deck
            card_to_move = deck_to_shuffle [randint(0, len(deck_to_shuffle) -1)]
            # put it in random deck
            deck_to_shuffle.remove(card_to_move)
            # now remove it from original deck
            shuffle_deck.append(card_to_move)
        return shuffle_deck

    

deck = Deck(NUMBERS, COLORS)
shuffled = deck.shuffle()
for card in shuffled
    print(card)




class Game:
    pass
