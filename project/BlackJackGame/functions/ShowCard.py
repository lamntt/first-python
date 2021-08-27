from models.Hand import Hand
def show_some(player,dealer):
    print("\n Dealer's Hand: ")
    print('< Hidden Card >')
    print(dealer.cards[1])
    print("\n Player's Hand: ",*player.cards,sep='\n')
def show_all(player,dealer):
    print("\n Dealer's Hand: ",*dealer.cards,sep='\n')
    print("\n Player's Hand: ",*player.cards,sep='\n')