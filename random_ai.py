import random

def random_ai(board, player):
    coordinates = [None, None]
    while True:
        x_coordinate = random.randint(0,2)
        y_coordinate = random.randint(0,2)
        if board[x_coordinate][y_coordinate] == None:
            coordinates[0], coordinates[1] = x_coordinate, y_coordinate
            return coordinates