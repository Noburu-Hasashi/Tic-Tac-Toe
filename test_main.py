from main import new_board

def test_new_board():
    expected_output = [
                        [None, None, None],
                        [None, None, None],
                        [None, None, None]
    ]
    actual_output = new_board()
    assert expected_output == actual_output