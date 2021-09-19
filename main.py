from game import *
import random

while True:
    board = new_board()  # constructs an empty board
    players = ['X', 'O']  # choses a random player to start the game
    player = players[random.randint(0, 1)]
    print("Player '", player, "' goes first!")
    render(board)
    for turn in range(9):  # makes the game run for 9 turns
        coordinates = get_move()
        make_move(coordinates, board, player)
        winner = get_winner(board)
        if winner == None:
            if turn == 8:
                print("- - -GAME ENDED! THIS GAME IS A DRAW!- - -")
                break
            if player == 'X':
                player = 'O'
            if player == 'O':
                player = 'X'
    break
