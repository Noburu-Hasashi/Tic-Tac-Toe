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

def get_move():  # asks user to input co-ordinates and returns them
    coordinates = (None, None)
    x_coordinate = input("Enter the value for X co-ordinate: ")
    y_coordinate = input("Enter the value for Y co-ordinate: ")
    coordinates[0], coordinates[1] = x_coordinate, y_coordinate
    return coordinates

def is_valid_move(x_coordinate, y_coordinate, board):  # checks if the coordinates provided by the user are valid or not
    if isinstance(x_coordinate, int) == True and isinstance(y_coordinate, int) == True:
        if len(str(x_coordinate)) == 1 and len(str(y_coordinate)) == 1:
            if board[x_coordinate][y_coordinate] == None:
                return True
    return False

def make_move(coordinates, board, player):  # makes a move by appending the board
    while True:
        if is_valid_move(coordinates[0], coordinates[1], board) == False:
            print("- - -ERROR! INVALID INPUT! TRY AGAIN!- - -")
            coordinates = get_move()
        elif is_valid_move(coordinates[0], coordinates[1], board) == True:
            break
    x_coordinate, y_coordinate = coordinates[0], coordinates[1]
    board[x_coordinate][y_coordinate] = player
        