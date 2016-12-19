import random

class Deck:
    Value = {'Ace':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10}
    suits = ['Hearts','Spades','Clubs','Diamonds']
    numbers = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    class card:
        def __init__(self, suit, face_or_number):
            self.suit = suit
            self.face_or_number = face_or_number

    # representaion when printed, javas toString override
        def __repr__(self):
            self.str_rep = self.face_or_number + ' of ' + self.suit
            return self.str_rep


    def __init__(self):
        self.deck = []
        # For every thing in the lists make a deck
        for suit in self.suits:
            i = suit
            for numberFace in self.numbers:
                j = numberFace
                self.deck.append(Deck.card(i, j))
        random.shuffle(self.deck)


    def print_whole_deck(self):
        for card in self.deck:
            print(card)


    def deal_card_to_player(self):
        # this method deals from the bottom of the deck ( I know that's not legal techinically but whatever)
        try:
            A_card = self.deck.pop()
            return A_card
        except IndexError:
            "The game experienced an unexpected error! There were no cards left!"