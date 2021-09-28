from game import *

def minimax_score(board, current_player):
    if get_winner(board) == current_player:
        return +10
    elif get_winner(board) != current_player:
        if get_winner(board) == None:
            return 0
        else:
            return -10

    