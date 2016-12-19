from Player import *
def Main():
    print("Welcome to simple game of BlackJack!!")
    ListPlayers = []

    def Print_Menu():
        print('(1): Play Game\n'
              '(2): Exit\n')


    while True:
        Print_Menu()
        user_choice = int(input("Please choose an Option.\n"))
        deck = Deck()
        if user_choice == 1:
            nameInput = Player(input('Please enter your name to play.\n'))
            ListPlayers.append(nameInput)
            for i in range(2):
                for players in ListPlayers:
                    players.hand.append(deck.deal_card_to_player())
                    players.display_hand()
            players.add_up_cards()
            while True:
                draw = input("Draw? type y or n")
                if draw == 'y':
                    players.hand.append(deck.deal_card_to_player())
                    players.display_hand()
                    players.amount = 0
                    players.add_up_cards()
                    if players.amount > 21:
                        print("You Lost, Game Over")
                        break
                    if players.amount == 21:
                        print("You Won, Congratulations!!!")
                        break
                    # elif players.amount != 21:
                    #     print("You Lost")
                    #     break
        elif user_choice == 2:
            break
Main()