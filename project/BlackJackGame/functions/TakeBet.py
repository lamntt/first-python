from models.Chips import Chips
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How much do you wanna bet? '))
        except:
            print('Please input an integer!')
        else:
            if chips.bet > chips.total:
                print('Sorry you dont have enough chips to bet')
                continue
            else:
                break








