# 1
def display_board(board):
    print("|" + board[1] + "|" + board[2] + "|" + board[3] + "|")
    print("|" + board[4] + "|" + board[5] + "|" + board[6] + "|")
    print("|" + board[7] + "|" + board[8] + "|" + board[9] + "|")


# test_board = [' ']*10
# display_board(test_board)
# 2
def player_input():
    player1_marker = ""
    while player1_marker not in ["X", "O"]:
        player1_marker = input("Player 1 pls select X or O: ")
    if player1_marker == "X":
        return ("X", "O")
    if player1_marker == "O":
        return ("O", "X")


# 3
def place_marker(board, mark, position):
    board[position] = mark


# 4
def win_check(board, mark):

    if (
        (board[7] == board[8] == board[9] == mark)
        or (board[4] == board[5] == board[6] == mark)
        or (board[1] == board[2] == board[3] == mark)
        or (board[1] == board[5] == board[9] == mark)
        or (board[3] == board[5] == board[7] == mark)
        or (board[1] == board[4] == board[7] == mark)
        or (board[2] == board[5] == board[8] == mark)
        or (board[3] == board[6] == board[9] == mark)
    ):
        return True
    else:
        return False


# 5
import random


def choose_first():
    first_player = random.randint(1, 2)
    if first_player == 1:
        return 1
    elif first_player == 2:
        return 2

    # 6


def space_check(board, position):
    if board[position] == " ":
        return True
    return False


# 7
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# 8
def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(
        board, position
    ):
        position = int(input("Pls choose position you want: "))
    return position


# 9
def replay():
    game_on = input("Do you want to replay the game?: ")
    if game_on == "Yes":
        return True
    else:
        return False


print("Welcome to TicTacToe game.")

while True:
    test_board = [" "] * 10
    display_board(test_board)

    player1_marker, player2_marker = player_input()

    turn = choose_first()
    if turn == 1:
        print("Player 1 will go first.")
    else:
        print("Player 2 will go first.")
    play_game = input("Are you ready to play the game? Y or N: ")
    if play_game == "Y":
        game_on = True
        # test_board = [' ']*10
    else:
        game_on = False

    while game_on:
        print("game replay")
        print(turn)
        if turn == 1:
            # print("Player 1 will")
            display_board(test_board)
            position = player_choice(test_board)
            # free_position = space_check(test_board,player1_position)
            # if free_position == True:
            place_marker(test_board, player1_marker, position)
            # win_game = win_check(test_board,player1_marker)
            if win_check(test_board, player1_marker):
                print("Player 1 won.")
                display_board(test_board)
                game_on = False
            else:
                # print("Player 1 is")
                if full_board_check(test_board):
                    display_board(test_board)
                    print("Gmae is full draw!")
                    break
                else:
                    # print("Player 1 turn")
                    turn = 2

        else:
            # print("Player 2 will")
            display_board(test_board)
            position = player_choice(test_board)
            # free_position = space_check(test_board,player1_position)
            # if free_position == True:
            place_marker(test_board, player2_marker, position)
            # win_game = win_check(test_board,player2_marker)
            if win_check(test_board, player2_marker):
                print("Player 2 won.")
                display_board(test_board)
                game_on = False
            else:
                # print("Player 2 is")
                if full_board_check(test_board):
                    display_board(test_board)
                    print("Gmae is full draw!")
                    break
                else:
                    # print("Player 2 turn")
                    turn = 1

    if not replay():
        break
