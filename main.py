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

def get_winner_from_XO_count(X_count, O_count):  # checks for the winner from both X_count and O_count
    if X_count == 3:
        return 'X'
    elif O_count == 3:
        return 'O'
    else:
        return None

def get_updated_XO_count(X_count, O_count, board, x_coordinate, y_coordinate):  # checks board and returns updated X_count and O_count
    if board[x_coordinate][y_coordinate] == 'X':
        X_count += 1
    elif board[x_coordinate][y_coordinate] == 'O':
        O_count += 1
    return X_count, O_count

def get_winner_from_rows_and_columns(board, is_column, X_count, O_count):  # checks for winner in rows and columns and returns the winner
    for row in range(3):
        X_count = 0
        O_count = 0
        for column in range(3):
            if is_column == False:
                X_count, O_count = get_updated_XO_count(X_count, O_count, board, row, column)  # checks for 'X' or 'O' in the rows
            elif is_column == True:
                X_count, O_count = get_updated_XO_count(X_count, O_count, board, column, row)  # checks for 'X' or 'O' in the columns
        if get_winner_from_XO_count(X_count, O_count) != None:
            return get_winner_from_XO_count(X_count, O_count)
    return None

def get_winner_from_diagonals(board, X_count, O_count):  # checks for winner in the two diagonals and returns the winner
    for i in range(3):
            X_count, O_count = get_updated_XO_count(X_count, O_count, board, i, i)  # checks for winner in the forward diagonal
    if get_winner_from_XO_count(X_count, O_count) == None:
        X_count = 0
        O_count = 0
        for i in range(3):
            X_count, O_count = get_updated_XO_count(X_count, O_count, board, i, 2-i)  # checks for winner in the backward diagonal
    return get_winner_from_XO_count(X_count, O_count)

def get_winner(board):  # checks for winner in the board and returns it
    row_result = get_winner_from_rows_and_columns(board, False, 0, 0)  # checks for winner in rows
    column_result = get_winner_from_rows_and_columns(board, True, 0, 0)  # checks for winner in columns
    diagonal_result = get_winner_from_diagonals(board, 0, 0)  # checks for winner in diagonals

    if row_result != None:
        return row_result
    elif column_result != None:
        return column_result
    elif diagonal_result != None:
        return diagonal_result

    return None