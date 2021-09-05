from main import new_board, is_valid_move

def test_new_board():
    expected_output = [
                        [None, None, None],
                        [None, None, None],
                        [None, None, None]
    ]
    actual_output = new_board()
    assert expected_output == actual_output

def test_is_valid_move():
    sample_board = [
                        ['X', None, 'O'],
                        [None, 'O', None],
                        ['X', None, 'X']
    ]
    assert is_valid_move('X', 1, sample_board) == False
    assert is_valid_move(0, 1, sample_board) == True
    assert is_valid_move(0, 2, sample_board) == False
    assert is_valid_move(1, 1, sample_board) == False
    assert is_valid_move(112, 0, sample_board) == False
    assert is_valid_move(2, 1, sample_board) == True
    assert is_valid_move(2, 122, sample_board) == False