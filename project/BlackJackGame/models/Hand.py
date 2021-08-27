from models.Card import values,ranks,suits
class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces +=1
    def adjust_for_aces(self):
        while self.value >21 and self.aces >0 :
            self.value -=10
            self.aces -=1
