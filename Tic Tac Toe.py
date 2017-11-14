print('Welcome to Tic Tac Toe!')
def display_board(board):
    print ' ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3]
    print '-------------'
    print ' ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6]
    print '-------------'
    print ' ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9]


def player_input():
    cursor = ''
    while not (cursor == 'X' or cursor == 'O'):
        cursor = raw_input( Player1 + ' Do you want to be X or O?').upper()
        if cursor == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')



def position(board, cursor, pos):
            board[pos] = cursor


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))
def player_name():
    Player1 = raw_input('Player 1 Enter your name:')
    Player2 = raw_input('Player 2 enter your name:')

import random


def random_player():
    if random.randint(0, 1) == 1:
        return Player1
    else:
        return Player2

def space_check(board, pos):
    return board[pos] == ' '


def board_full(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def next_pos(board):
    pos = ''
    while pos not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(pos)):
        pos = raw_input('Choose your next position: (1-9) ')
    return int(pos)


def replay():
    return raw_input('Do you want to play again? Enter Yes or No ').lower().startswith('yes')



while True:
    Player1=raw_input('Player 1 Enter your name:')
    Player2=raw_input('Player 2 Enter your name:')
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    print Player1 + ' you are '+ player1_marker
    print Player2 + ' you are '+ player2_marker
    turn = random_player()
    print turn + ' will go first.'
    game_on = True

    while game_on==True:
        if turn == Player1:
            display_board(theBoard)
            pos = next_pos(theBoard)
            position(theBoard, player1_marker, pos)
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print 'Congratulations! ' + Player1 + '  has won the game!'
                game_on = False
            else:
                if board_full(theBoard):
                    display_board(theBoard)
                    print 'The game is a draw!'
                    game_on=False
                    break
                else:
                    turn = Player2


        else:
            display_board(theBoard)
            pos = next_pos(theBoard)
            position(theBoard, player2_marker, pos)
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print 'Congratulations! ' + Player2 + ' has won the game! '
                game_on = False
            else:
                if board_full(theBoard):
                    display_board(theBoard)
                    print 'The game is a tie!'
                    game_on=False
                    False
                    break
                else:
                    turn = Player1

    if not replay():
        break
