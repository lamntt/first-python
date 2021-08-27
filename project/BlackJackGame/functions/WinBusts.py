from models.Chips import Chips
def player_busts( chips):
    print('Player BUSTS. Dealer win.')
    chips.lose_bet()
def dealer_busts(chips):
    print('Dealer BUSTS. Player win')
    chips.win_bet()
def player_win(chips):
    print('Player greater. Player win!')
    chips.win_bet()
def dealer_win(chips):
    print('Dealer greater. Dealer win!')
    chips.lose_bet()
def push(chips):
    print('It is TIE')