#1
def display_board(board) :
  print('|'+board[1]+'|'+board[2]+'|'+board[3]+'|')
  print('|'+board[4]+'|'+board[5]+'|'+board[6]+'|')
  print('|'+board[7]+'|'+board[8]+'|'+board[9]+'|')
test_board = ['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
# display_board(test_board)



#2
def player_input():
  marker = 'wr'
  while marker not in ['X','O']:
    marker = input('Player 1 pls choose X or O: ')
    if marker not in ['X','O']:
      print('Pls choose between X and O')
    # if marker == 'X':
    #   player1_marker = marker
    #   player2_marker = 'O'
    # elif marker == 'O':
    #   player1_marker = marker
    #   player2_marker = 'X'
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
  # return (player1_marker, player2_marker)
# print(player_input())
# player_choice = player_input()

#3
position_list = [1,2,3,4,5,6,7,8,9]
def place_marker(board, marker, position):
  board[position]=marker
  # for num in position_list:
  #     board[num] = marker
  # player_position = 'wr'
  # # player2_position = 'fl'
  # while player_position not in position:
  #   player_position = int(input(' pls choose your position 1 to 9 : '))
  #   test_board[player_position]= 
  #   display_board(test_board)
  # while player2_position not in position:
  #   player2_position = int(input('Player 2 pls choose your position 1 to 9 : '))
  #   test_board[player2_position]= player_choice[1]
  #   display_board(test_board)

# place_marker(test_board,player_choice,position)

#4
def win_check(board, mark):
  # for any_board in test_board:
  if ((board[7] == board[8] == board[9] == mark ) or 
    (board[4] == board[5] == board[6] == mark) or 
    (board[1] == board[2] == board[3] == mark) or 
    (board[1] == board[5] == board[9] == mark) or 
    (board[3] == board[5] == board[7] == mark) or 
    (board[1] == board[4] == board[7] == mark) or 
    (board[2] == board[5] == board[8] == mark) or 
    (board[3] == board[6] == board[9] == mark) ):
    return True
  return False
  # elif  (board[7] == board[8] == board[9] == player_choice[1]  or \
  #   board[4] == board[5] == board[6] == player_choice[1] or \
  #   board[1] == board[2] == board[3] == player_choice[1] or \
  #   board[1] == board[5] == board[9] == player_choice[1] or \
  #   board[3] == board[5] == board[7] == player_choice[1] ):
  #   print('Player 2 win')
  # else:
  #   print('Both player are lose')



#5
from random import randint

def choose_first():
  rand_player = randint(1,2)
  # first_player = input(f'Player {rand_player} go first')
  return rand_player
# choose_first() 



#6
# def space_check(board, position):
#   return board[position] == ' '


# #7
# def full_board_check(board):
#   for num in board:
#     if num==" ":
#       return False
#   return True

def space_check(board, position):
    
    return board[position] == ' '



def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
    # for i in range(1,10):
    #     if space_check(board, i):
    #         return False
    # return True




#8
# free_position = space_check(test_board, position)
def player_choice(board):
  position = 0
    
  while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
      position = int(input('Choose your next position: (1-9) '))
      
  return position

#9 

def replay():
  continues = ''
  while continues not in ['Y', 'N'] :
    continues = input('Do you want  to play again, type Y or N: ')
    if continues not in ['Y', 'N']:
      print('Pls choose Y or N.')
    
  if continues == 'Y':
    return True
  return False



print('Welcome to Tic Tac Toe!')

while True:
  player1_marker, player2_marker = player_input()
  turn = choose_first()
  print(f'Player {turn} go first')
  play_game = input('Are you ready to play? Enter Yes or No.')
    
  if play_game.lower()[0] == 'y':
    game_on = True
    test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
  else:
    game_on = False



  while game_on == True:
    if turn == 1:
      display_board(test_board)
    
      position = player_choice(test_board)
      place_marker(test_board, player1_marker, position)

      if win_check(test_board, player1_marker):
          display_board(test_board)
          print('Congratulations! You have won the game!')
          game_on = False
      else:
          if full_board_check(test_board):
              display_board(test_board)
              print('The game is a draw!')
              break
          else:
              turn = 2

    else:
            # Player2's turn.
            
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board, player2_marker, position)

            if win_check(test_board, player2_marker):
                display_board(test_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 1

  if not replay():
    break


      















