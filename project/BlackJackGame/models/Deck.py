from models.Card import suits,ranks,random,Card
class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal(self):
        return self.all_cards.pop()
























