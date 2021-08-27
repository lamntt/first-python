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


# test_deck = Deck()
# test_deck.shuffle()
# dealcard= test_deck.deal()
# print(dealcard)


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Aces":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# hand_card = Hand()
# hand_card.add_card(test_deck.deal())
# hand_card.add_card(test_deck.deal())

# print(hand_card.value)5


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# chips = Chips()


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How much do you wanna bet: "))
        except:
            print("Sorry! Please take an integer value.")
        else:
            if chips.bet > chips.total:
                print("Your chips is not enough!")
            else:
                break


# chip = Chips()
# take_bet(chip)
# print(chip.bet)


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


playing = True
# playing = True
def hit_or_stand(deck, hand):
    global playing
    while True:
        go_hit = input("Would you wnana hit? Hit or Stand: ")
        if go_hit[0] == "h":
            hit(deck, hand)
        elif go_hit[0] == "s":
            playing = False
        else:
            print("Sorry! Please choose Hit or Stand again!")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print("", dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep="\n ")


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n ")
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    # if player.value > 21:
    print("Player busts! Dealer Win.")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    # if player.value > dealer.value:
    print("Player's value is geater. Player Win!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    # if dealer.value > 21:
    print("Dealer busts! Player Win.")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    # if player.value < dealer.value:
    print("Dealer's value is geater. Dealer Win!")
    chips.lose_bet()


def push(player, dealer):
    print("No one Win this match! It's a tie.")


chips = Chips()
while True:
    # Print an opening statement
    print("Welcome to BlackJack game!")

    # Create & shuffle the deck, deal two cards to each player
    new_deck = Deck()
    new_deck.shuffle()

    player = Hand()
    player.add_card(new_deck.deal())
    player.add_card(new_deck.deal())

    dealer = Hand()
    dealer.add_card(new_deck.deal())
    dealer.add_card(new_deck.deal())

    # Set up the Player's chips

    # Prompt the Player for their bet
    take_bet(chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player, dealer)

    while playing:

        # Prompt for Player to Hit or Stand
        hit_or_stand(new_deck, player)

        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(player, dealer, chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    # print("bet:" + str(chips.bet))
    # print("total:" + str(chips.total))
    if player.value <= 21:

        while dealer.value < 17:
            hit(new_deck, dealer)

        # Show all cards
        show_all(player, dealer)
        # Run different winning scenarios
        if dealer.value > 21:
            dealer_busts(player, dealer, chips)
        elif player.value > dealer.value:
            player_wins(player, dealer, chips)
        elif player.value < dealer.value:
            dealer_wins(player, dealer, chips)
        else:
            push(player, dealer)

    # Inform Player of their chips total

    print("Player currently total is: ", chips.total)
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == "y":
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
        # break
