# imports the board manager class
from random import randint

from board_manager import BoardManager

# from server import Server
ship_list = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
ship_direction = ["Horizontal", "Vertical"]
ship_right_left_down_up = ["Right", "Left", "Up", "Down"]
board = BoardManager()


# Method to check if the player has inserted all of their ships onto the board
def isEmpty(list):
    if ship_list:
        return True
    else:
        return False


def setup_ships(ship_direction, ship_right_left_down_up):
    ship_selected = ship_list.pop(randint(0, len(ship_list - 1)))  # pops a random ship to insert
    ship_direction_selected = ship_direction(randint(0, len(ship_direction - 1)))  # selects a random ship direction
    # selects randomly what way a ship will go from its starting location
    ship_right_left_down_up_selection = ship_right_left_down_up(randint(0, len(ship_right_left_down_up - 1)))
    rand_x = randint(1, 11)  # sets a random x in matrix
    rand_y = randint(1, 11)  # sets a random y in matrix
    # runs if statement if the ship will fit
    if board.does_ship_fit(ship_selected, ship_direction_selected, ship_right_left_down_up_selection, rand_x, rand_y):
        # inserts ship into the board
        board.insert_ships(ship_selected, ship_direction_selected, ship_right_left_down_up_selection, rand_x, rand_y)
    else:
        ship_list.append(ship_selected)  # appends the ship that didn't fit back into the list

    class Player:
        while not isEmpty(ship_list):
            setup_ships(ship_direction, ship_right_left_down_up)
