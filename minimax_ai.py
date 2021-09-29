from game import *

def get_legal_moves(board):
    moves = []
    for row in range(3):
        for column in range(3):
            if board[row][column] == None:
                moves.append([row, column])
    return moves

def minimax_score(board, current_player):
    if get_winner(board) == current_player:
        return +10
    elif get_winner(board) != current_player:
        if get_winner(board) == None:
            return 0
        else:
            return -10