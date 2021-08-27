# from models.Card import playing
from models.Hand import Hand


def hit(hand,deck):
    hand.add_card(deck.deal())
    hand.adjust_for_aces()
def hit_or_stand(hand,deck):
    # global playing
    playing=True
    while True:
        play = input('Hit or Stand: ')
        if play[0].lower() == 'h':
            hit(hand,deck)
            # return True
            playing= True
            
        elif play[0].lower() == 's':
            # return False
            playing=False
            break
            
        else:
            print(' hit or stand pls! ')
            continue
        break
    return playing

