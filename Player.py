from Deck import *
class Player:
    def __init__(self, name):
        self.hand = []
        self.amount = int(0)
        self.name = name

#Shows the players hands
    def display_hand(self):
        counter = 0
        for card in self.hand:
            print("-[{}]--> {}".format(counter + 1, card))
            counter += 1
        print('-----------------------------------')

    def __rpr__(self):
        return str(self.name)

    def name_score(self):
        return self.name + '\'s score:' + str(self.amount)

    def add_up_cards(self):
        totalAmount = 0
        for A_card in self.hand:
            if A_card.face_or_number in Deck.Value:
                point_value = Deck.Value.get(A_card.face_or_number)
                self.amount += point_value

        print(str(self.name_score()))
        return self.amount