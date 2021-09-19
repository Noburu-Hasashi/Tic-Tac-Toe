from game import *
import random

board = new_board()  # constructs an empty board
players = ['X', 'O']  # choses a random player to start the game
current_player = players[random.randint(0, 1)]
print("Player '", current_player, "' goes first!")
render(board)
for turn in range(9):  # makes the game run for 9 turns
    print("ENTER COORDINATES FOR PLAYER ", current_player, ":")
    coordinates = get_move()
    make_move(coordinates, board, current_player)
    render(board)
    winner = get_winner(board)
    if winner == None:
        if turn == 8:
            print("- - -GAME ENDED! THIS GAME IS A DRAW!- - -")
            break
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    if winner == 'X':
        print("- - -GAME ENDED! PLAYER 'X' IS THE WINNER!- - -")
        break
    if winner == 'O':
        print("- - -GAME ENDED! PLAYER 'O' IS THE WINNER!- - -")
        break