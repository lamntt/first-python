import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


# new_card = Card('Hearts','Two')
# print(new_card)


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop()

    # def __str__(self):
    #     return self.all_cards


test_deck = Deck()
test_deck.shuffle()
# dealcard= test_deck.deal()
# print(dealcard)


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Aces':
            self.aces += 1
    def adjust_for_ace(self):
        while self.value > 21 and self.aces :
            self.value -= 10
            self.aces -=1


hand_card = Hand()
hand_card.add_card(test_deck.deal())
hand_card.add_card(test_deck.deal())

print(hand_card.value)
for ca in hand_card.cards:
    print(ca)


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How much do you wanna bet: '))
        except:
            print('Sorry! Please take an integer value.')
        else:
            if chips.bet > chips.total:
                print('Your chips is not enough!')
            else:
                break

chip = Chips()
take_bet(chip)
print(chip.bet)






























































