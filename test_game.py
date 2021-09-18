from game import new_board, is_valid_move, get_winner_from_XO_count, get_updated_XO_count, get_winner_from_rows_and_columns, get_winner_from_diagonals, get_winner


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


def test_get_winner_from_XO_count():
    assert get_winner_from_XO_count(0, 0) == None
    assert get_winner_from_XO_count(1, 2) == None
    assert get_winner_from_XO_count(3, 0) == 'X'
    assert get_winner_from_XO_count(0, 3) == 'O'
    assert get_winner_from_XO_count(4, 7) == None


def test_get_updated_XO_count():
    sample_board = [
        ['X', None, 'O'],
        ['O', 'O', 'O'],
        ['X', None, 'X']
    ]
    get_updated_XO_count(0, 0, sample_board, 0, 0) == (1, 0)
    get_updated_XO_count(2, 1, sample_board, 0, 1) == (2, 1)
    get_updated_XO_count(0, 0, sample_board, 0, 2) == (0, 1)
    get_updated_XO_count(3, 2, sample_board, 1, 0) == (3, 3)
    get_updated_XO_count(1, 1, sample_board, 1, 1) == (1, 2)
    get_updated_XO_count(8, 5, sample_board, 1, 2) == (8, 6)
    get_updated_XO_count(9, 2, sample_board, 2, 0) == (10, 2)
    get_updated_XO_count(3, 4, sample_board, 2, 1) == (3, 4)
    get_updated_XO_count(8, 3, sample_board, 2, 2) == (9, 3)


def test_get_winner_from_rows_and_columns():
    sample_board = [
        ['X', None, 'O'],
        ['O', 'O', 'O'],
        ['X', None, 'X']
    ]
    assert get_winner_from_rows_and_columns(sample_board, False, 0, 0) == 'O'
    assert get_winner_from_rows_and_columns(sample_board, True, 0, 0) == None
    sample_board = [
        ['O', None, 'X'],
        [None, 'O', None],
        ['X', None, 'X']
    ]
    assert get_winner_from_rows_and_columns(sample_board, False, 0, 0) == None
    assert get_winner_from_rows_and_columns(sample_board, True, 0, 0) == None
    sample_board = [
        ['O', 'O', 'O'],
        [None, 'O', None],
        ['X', None, 'X']
    ]
    assert get_winner_from_rows_and_columns(sample_board, False, 0, 0) == 'O'
    assert get_winner_from_rows_and_columns(sample_board, True, 0, 0) == None
    sample_board = [
        ['O', 'O', None],
        [None, 'O', None],
        ['X', 'O', 'X']
    ]
    assert get_winner_from_rows_and_columns(sample_board, False, 0, 0) == None
    assert get_winner_from_rows_and_columns(sample_board, True, 0, 0) == 'O'
    sample_board = [
        ['O', 'O', None],
        [None, 'O', None],
        ['X', None, 'O']
    ]
    assert get_winner_from_rows_and_columns(sample_board, False, 0, 0) == None
    assert get_winner_from_rows_and_columns(sample_board, True, 0, 0) == None
    sample_board = [
        ['X', 'O', None],
        ['X', None, None],
        ['X', 'O', 'X']
    ]
    assert get_winner_from_rows_and_columns(sample_board, False, 0, 0) == None
    assert get_winner_from_rows_and_columns(sample_board, True, 0, 0) == 'X'
    sample_board = [
        ['O', 'O', 'X'],
        [None, None, 'X'],
        ['X', 'O', 'X']
    ]
    assert get_winner_from_rows_and_columns(sample_board, False, 0, 0) == None
    assert get_winner_from_rows_and_columns(sample_board, True, 0, 0) == 'X'
    sample_board = [
        ['O', 'O', None],
        ['O', 'O', 'O'],
        ['X', None, 'X']
    ]
    assert get_winner_from_rows_and_columns(sample_board, False, 0, 0) == 'O'
    assert get_winner_from_rows_and_columns(sample_board, True, 0, 0) == None
    sample_board = [
        ['O', 'O', None],
        [None, 'O', None],
        ['X', 'X', 'X']
    ]
    assert get_winner_from_rows_and_columns(sample_board, False, 0, 0) == 'X'
    assert get_winner_from_rows_and_columns(sample_board, True, 0, 0) == None
    sample_board = [
        ['O', 'O', 'X'],
        [None, 'X', None],
        ['X', 'O', 'X']
    ]
    assert get_winner_from_rows_and_columns(sample_board, False, 0, 0) == None
    assert get_winner_from_rows_and_columns(sample_board, True, 0, 0) == None
    sample_board = [
        ['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['X', 'X', 'O']
    ]
    assert get_winner_from_rows_and_columns(sample_board, False, 0, 0) == None
    assert get_winner_from_rows_and_columns(sample_board, True, 0, 0) == None
    sample_board = [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        ['O', 'X', 'X']
    ]
    assert get_winner_from_rows_and_columns(sample_board, False, 0, 0) == None
    assert get_winner_from_rows_and_columns(sample_board, True, 0, 0) == None

def test_get_winner_from_diagonals():
    sample_board = [
        ['X', None, 'O'],
        ['O', 'O', 'O'],
        ['X', None, 'X']
    ]
    assert get_winner_from_diagonals(sample_board, 0, 0) == None
    sample_board = [
        ['O', None, 'X'],
        [None, 'O', None],
        ['X', None, 'X']
    ]
    assert get_winner_from_diagonals(sample_board, 0, 0) == None
    sample_board = [
        ['O', 'O', 'O'],
        [None, 'O', None],
        ['X', None, 'X']
    ]
    assert get_winner_from_diagonals(sample_board, 0, 0) == None
    sample_board = [
        ['O', 'O', None],
        [None, 'O', None],
        ['X', 'O', 'X']
    ]
    assert get_winner_from_diagonals(sample_board, 0, 0) == None
    sample_board = [
        ['O', 'O', None],
        [None, 'O', None],
        ['X', None, 'O']
    ]
    assert get_winner_from_diagonals(sample_board, 0, 0) == 'O'
    sample_board = [
        ['X', 'O', None],
        ['X', None, None],
        ['X', 'O', 'X']
    ]
    assert get_winner_from_diagonals(sample_board, 0, 0) == None
    sample_board = [
        ['O', 'O', 'X'],
        [None, None, 'X'],
        ['X', 'O', 'X']
    ]
    assert get_winner_from_diagonals(sample_board, 0, 0) == None
    sample_board = [
        ['O', 'O', None],
        ['O', 'O', 'O'],
        ['X', None, 'X']
    ]
    assert get_winner_from_diagonals(sample_board, 0, 0) == None
    sample_board = [
        ['O', 'O', None],
        [None, 'O', None],
        ['X', 'X', 'X']
    ]
    assert get_winner_from_diagonals(sample_board, 0, 0) == None
    sample_board = [
        ['O', 'O', 'X'],
        [None, 'X', None],
        ['X', 'O', 'X']
    ]
    assert get_winner_from_diagonals(sample_board, 0, 0) == 'X'
    sample_board = [
        ['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['X', 'X', 'O']
    ]
    assert get_winner_from_diagonals(sample_board, 0, 0) == 'X'
    sample_board = [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        ['O', 'X', 'X']
    ]
    assert get_winner_from_diagonals(sample_board, 0, 0) == None

def test_get_winner():
    sample_board = [
        ['X', None, 'O'],
        ['O', 'O', 'O'],
        ['X', None, 'X']
    ]
    assert get_winner(sample_board) == 'O'
    sample_board = [
        ['O', None, 'X'],
        [None, 'O', None],
        ['X', None, 'X']
    ]
    assert get_winner(sample_board) == None
    sample_board = [
        ['O', 'O', 'O'],
        [None, 'O', None],
        ['X', None, 'X']
    ]
    assert get_winner(sample_board) == 'O'
    sample_board = [
        ['O', 'O', None],
        [None, 'O', None],
        ['X', 'O', 'X']
    ]
    assert get_winner(sample_board) == 'O'
    sample_board = [
        ['O', 'O', None],
        [None, 'O', None],
        ['X', None, 'O']
    ]
    assert get_winner(sample_board) == 'O'
    sample_board = [
        ['X', 'O', None],
        ['X', None, None],
        ['X', 'O', 'X']
    ]
    assert get_winner(sample_board) == 'X'
    sample_board = [
        ['O', 'O', 'X'],
        [None, None, 'X'],
        ['X', 'O', 'X']
    ]
    assert get_winner(sample_board) == 'X'
    sample_board = [
        ['O', 'O', None],
        ['O', 'O', 'O'],
        ['X', None, 'X']
    ]
    assert get_winner(sample_board) == 'O'
    sample_board = [
        ['O', 'O', None],
        [None, 'O', None],
        ['X', 'X', 'X']
    ]
    assert get_winner(sample_board) == 'X'
    sample_board = [
        ['O', 'O', 'X'],
        [None, 'X', None],
        ['X', 'O', 'X']
    ]
    assert get_winner(sample_board) == 'X'
    sample_board = [
        ['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['X', 'X', 'O']
    ]
    assert get_winner(sample_board) == 'X'
    sample_board = [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        ['O', 'X', 'X']
    ]
    assert get_winner(sample_board) == None