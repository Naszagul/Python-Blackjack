"""
Computer dealer and one Human player

Normal deck of cards

Player has bankroll
Player places a bet
dealer stars with 1 card face up and 1 face down.
player starts with 2 cards face up

player can hit or stay only
blackjack simplified

computer hits until player is beat or computer busts

face cards = 10
aces = 1 or 11

"""

import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

    def get_value(self):
        return self.value

    def display_card(self):
        print(f' ---- ')
        print(f'|{self.rank[0:3]} |')
        print(f'|   {self.suit[0]}|')
        print(f' ---- ')


class Deck():

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

    def deck(self):
        return self.all_cards


class Player:

    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # multiple cards
            self.all_cards.extend(new_cards)
        else:
            # single card
            self.all_cards.append(new_cards)

    def add_chips(self, chips):
        self.chips += chips

    def remove_chips(self, chips):
        if self.chips >= chips:
            self.chips -= chips
        else:
            print(f'{self.name}, you do not have enough chips for that bet!')
            raise

    def get_chips(self):
        return self.chips

    def __str__(self):
        return f'{self.name} has {self.chips} chips.'


def replay():
    choice = ''
    choices = ['Y', 'N']
    while choice not in choices:
        choice = input('Would you like to play again? (Y or N) ')
        if choice.upper() not in choices:
            print('\n' * 100)
            print('Invalid Response.')
        else:
            return choice.upper() == 'Y'


def Blackjack():
    global bet
    name = input('Welcome to Blackjack! \nPlease enter your name: ')
    dealer = Deck()
    dealer.shuffle()

    player = Player(name, 100)

    game_on = True

    while game_on:
        if player.get_chips() > 0:
            # place bet
            try:
                print(f'You have {player.get_chips()} total chips.')
                bet = abs(int(input('Place your bet ')))
                player.remove_chips(bet)

            except:
                print('Invalid response.')

            else:
                # dealer deal self 2 cards, second one face down
                if len(dealer.all_cards) < 15:
                    dealer = Deck()
                    dealer.shuffle()
                    print('Shuffling new deck...')
                house = [dealer.deal_one(), dealer.deal_one()]
                print('\n' * 100)
                print('Deal please!')
                print("Dealer hand:")
                house[0].display_card()
                print(""" ----
|    |
|    |
 ----""")
                print('_______________')
                # dealer deal 2 cards for player face up
                print(f"{player.name}'s hand: ")
                hand = [dealer.deal_one(), dealer.deal_one()]
                # while player not bust

                # input player hit or stay
                hit = ''
                stay = False
                bust = False
                blackjack = False
                hand_tot = 0
                while not bust or not stay:

                    if stay:
                        break

                    hand_tot = sum([hand[i].get_value() for i in range(len(hand))])

                    if hand_tot > 21:
                        for i in range(len(hand)):
                            if hand[i].get_value() == 11:
                                hand_tot -= 10

                    for i in range(len(hand)):
                        hand[i].display_card()
                    print(f'total: {hand_tot}')

                    bust = hand_tot > 21

                    # if bust, dealer wins round.
                    if bust:
                        print('Sorry you busted!')
                        break

                    elif hand_tot == 21:
                        if len(hand) == 2:
                            blackjack = True
                            break
                        else:
                            stay = True
                            break
                    else:
                        while hit != 'S':
                            hit = input('(H)it or (S)tay?: ').upper()
                            # if hit, dealer deal player one card
                            if hit == 'H':
                                hand.append(dealer.deal_one())
                                break
                            # if stay, player keeps current hand and ends round
                            if hit == 'S':
                                print('\n' * 100)
                                print('Staying with hand:')
                                for i in range(len(hand)):
                                    hand[i].display_card()
                                print(f'Your total: {hand_tot}')
                                stay = True

                            else:
                                print('Invalid Response.')

                if stay:
                    input("Dealer's turn, enter to continue. ")
                    print('\n' * 20)
                    # if dealer bust, player wins.
                    dealerbust = False
                    tie = False
                    dealerwin = False
                    while not dealerbust or not tie:

                        house_tot = sum([house[i].get_value() for i in range(len(house))])

                        if house_tot > 21:

                            for i in range(len(house)):

                                if house[i].get_value() == 11:
                                    house_tot -= 10

                        for i in range(len(house)):
                            house[i].display_card()

                        print(f'Dealer total: {house_tot}')
                        tie = house_tot == hand_tot <= 21
                        dealerbust = house_tot > 21
                        dealerwin = house_tot > hand_tot <= 21
                        if dealerbust:
                            break

                        elif tie:
                            break

                        elif dealerwin:
                            break
                        else:
                            house.append(dealer.deal_one())
                            print('dealer draws...')
                            input('enter to continue. ')

                    # if player stay's, dealer hits until either bust or hand value > player hand value

                    if tie:
                        player.add_chips(bet)
                        print('Tie!')
                        print('you keep your chips.')

                    elif dealerwin and not dealerbust:
                        print('Dealer wins.')
                        print('sorry, you lose.')
                        pass

                    else:
                        player.add_chips(bet * 2)
                        print('Dealer bust! you win 2x your bet!')
                        print(f'you have won {bet * 2} chips!')

                # if BlackJack(total value == 21 from first two cards player wins 3x bet
                elif blackjack:
                    player.add_chips(bet * 3)
                    print('Blackjack! you win 3x your bet!')
                    print(f'you have won {bet * 3} chips!')

        else:
            print('Sorry your out of chips!')
            break

    print('Game over!')

    ask = replay()
    if ask:
        Blackjack()


Blackjack()
