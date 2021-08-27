

from models.Card import playing
from models.Deck import Deck
from models.Hand import Hand
from models.Chips import Chips
from functions.Hit import hit,hit_or_stand
from functions.TakeBet import take_bet
from functions.WinBusts import player_busts,player_win,dealer_busts,dealer_win,push
from functions.ShowCard import show_all,show_some


chips = Chips()
while True:
    print('Welcome to BJ Game!')
    new_deck = Deck()
    new_deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(new_deck.deal())
    player_hand.add_card(new_deck.deal())
    dealer_hand = Hand()
    dealer_hand.add_card(new_deck.deal())
    dealer_hand.add_card(new_deck.deal())
    
    take_bet(chips)

    show_some(player_hand,dealer_hand)
    while playing:
        playing=hit_or_stand(player_hand,new_deck)
        # player_hand.adjust_for_aces()
        show_some(player_hand,dealer_hand)
        if player_hand.value > 21:
            show_all(player_hand,dealer_hand)
            player_busts(chips)
            break
    if player_hand.value <=21:
        while dealer_hand.value <17:
            hit(dealer_hand,new_deck)
        show_all(player_hand,dealer_hand)
        if dealer_hand.value >21:
            dealer_busts(chips)
            # show_all(player_hand,dealer_hand)
        elif player_hand.value > dealer_hand.value:
            player_win(chips)
            # show_all(player_hand,dealer_hand)
        elif player_hand.value < dealer_hand.value:
            dealer_win(chips)
            # show_all(player_hand,dealer_hand)
        else:
            push(chips)
            # show_all(player_hand,dealer_hand)

    print(chips.total)
    play_again = input('Do you wanna continue to play? y/n please: ')
    if play_again[0] == 'y':
        playing = True
        continue
    elif play_again == 'n':
        playing = False
        break


