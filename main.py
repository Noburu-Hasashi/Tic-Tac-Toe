from game import *
import random

def get_input_type():
	while True:
		try:
			player_1_input = int(input('''Enter the number for the type of input for player 1 :
	1. Asks user for input
	2. Random AI
	3. Winning AI'''))
			if len(str(player_1_input)) != 1:
				raise ValueError
			player_2_input = int(input('''Enter the number for the type of input for player 2 :
	1. Asks user for input
	2. Random AI
	3. Winning AI'''))
			if len(str(player_2_input)) != 1:
				raise ValueError
		except(ValueError, TypeError, SyntaxError):
			print("- - -ERROR! INVALID INPUT! TRY AGAIN!- - -")
		finally:
			return player_1_input, player_2_input

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