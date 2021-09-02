def new_board():  # creates a 2D array which represents the tic-tac-toe board
    board = []
    for row in range(3):
        board.append([None]*3)
    return board

def render(board):  # gives an output of the board on the terminal
    divider_string = '= ' * 6
    print(divider_string)
    for row in range(len(board)):
        print("|", board[row][0], end='')
        print("|", board[row][1], end='')
        print("|", board[row][2], "|")
        print(divider_string)
    print()