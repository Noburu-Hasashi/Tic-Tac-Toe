from winning_ai import *

def test_finds_winning_moves_ai():
	sample_board = [
		['X', 'O', None],
		[None, 'O', None],
		['X', None, None]
	]
	assert finds_winning_moves_ai(sample_board, 'X') == [1,0]
	sample_board = [
		['O', None, None],
		['O', None, None],
		[None, None, None]
	]
	assert finds_winning_moves_ai(sample_board, 'O') == [2,0]
	sample_board = [
		['O', 'O', None],
		['X', None, None],
		[None, None, None]
	]
	assert finds_winning_moves_ai(sample_board, 'O') == [0,2]
	sample_board = [
		['X', None, 'O'],
		[None, 'O', None],
		['X', None, None]
	]
	assert finds_winning_moves_ai(sample_board, 'X') == [1,0]
	sample_board = [
		['O',None, 'X'],
		[None, 'X', None],
		['O', None, None]
	]
	assert finds_winning_moves_ai(sample_board, 'O') == [1,0]