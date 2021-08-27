gameList = [0,1,2]
def display_game(gameList ):
    print("Here is the current list")
    print(gameList)
# display_game(gameList )



def choose_positions():
  choose = 'wr'
  while choose not in ['0','1','2']: 
   
    choose = input('Please choose your position you want to replace in (0,1,2): ')
    if choose not in ['0','1','2']:
      print('Please choose again')
  
  return int(choose)



# positions = choose_positions4() 
def input_replace(gameList,positions):
  yourReplacement = input('please type your replacement for that position: ')
  gameList[positions] = yourReplacement
  return gameList
# print(input_replace(gameList,positions))




def game_on():
  continues = 'wr'
  while continues not in ['Y', 'N'] :
    continues = input('Do you want to continue to play, type Y or N: ')
    if continues not in ['Y', 'N']:
      print('Pls choose Y or N.')
    
  if continues == 'Y':
    return True
  else :
    return False
  


gameOn = True
gameList = [0,1,2]
while gameOn :
  display_game(gameList)
  positions = choose_positions() 
  gameList = input_replace(gameList,positions)
  display_game(gameList )
  gameOn  = game_on()






