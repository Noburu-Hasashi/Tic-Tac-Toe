from winning_ai import *

def test_finds_winning_moves_ai():
    sample_board = [
        ['X', 'O', None],
        [None, 'O', None],
        ['X', None, None]
    ]
    assert finds_winning_moves_ai(sample_board, 'X') == [1,0]