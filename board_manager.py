import sys

length, width = 12, 11
coordinate_letters = 'ABCDEFGHIJ'
matrix = [[0 for x in range(width)] for y in range(length)]


def get_ship_length(self, ship):
    if ship == "Carrier":
        return 5
    elif ship == "Battleship":
        return 4
    elif ship == "Cruiser" or ship == "Submarine":
        return 3
    elif ship == "Destroyer":
        return 1
    else:
        print("Bad ship given, no value")


class BoardManager(object):

    def start_board(self):  # This method fills an array to create a clear game board.
        for i in range(0, width - 1):
            for j in range(0, length - 1):
                if j == 0 and i > 0:  # If left side of the board , then put in coordinate system.
                    matrix[i][j] = coordinate_letters[i]
                elif i == 0 and j > 0:  # If top of the board, then put in coordinate system.
                    matrix[i][j] = j
                elif i == 0 and j == 0:  # If top left corner, then put a space.
                    matrix[i][j] = ' '
                else:  # Playing field
                    matrix[i][j] = '~'


pass


def print_board(self):  # Prints the board into a file
    sys.stdout = open('own_board.txt', 'w')
    for i in range(0, width - 1):
        for j in range(0, length - 1):
            print(matrix[i][j], end=" ")
        print()


pass


def convert_user_input(x, y):  # Converts the users inputs into operable matrix inputs
    if x.isalpha():  # tests if first input is a character.
        found = False
        while not found:  # validation for input. NOTE!!! may not need, could cause infinite loop too
            for i in coordinate_letters:  # Iterates through coordinate string to find correct value for matrix.
                if x == coordinate_letters[i]:  # May need to adjust parameters .
                    new_x = i
                    found = True
    else:
        print('coordinate X invalid')
    if not y.isint():
        print('coordinate Y invalid')
    else:
        hit = check_if_hit(new_x, y)
    return hit


pass


# Method to check if the ship will fit in the board
def does_ship_fit(self, ship, direction, left_right_up_down, location_x, location_y):
    ship_length = get_ship_length(self, ship)  # gets the length of the ship that is trying to get inserted
    if direction == "horizontal":  # Checks if the ship is going to be inserted horizontally

        if left_right_up_down == "Right":  # checks to see if the ship is being inserted to the right of the initial location
            if (
                    width - 1) - location_x >= ship_length and location_x != 0:  # checks that the ship falls in the board and will fit
                for i in range(location_x,
                               width):  # loops to make sure the ship wont interfere with a ship already on the board
                    if matrix[i, location_y] != "_":
                        return False  # returns a false that the ship cannot be inserted
                else:
                    return True  # returns true if the ship can be inserted
            else:
                return False  # returns a false that the ship cannot be inserted
        if left_right_up_down == "Left":  # checks that the shift is being placed to the left of the initial peg
            if location_x - 1 >= ship_length and location_x != 0:  # checks that the ship falls in the board and will fit
                for i in reversed(range(location_x, 0)):  # checks to make sure the ship will fit.  loops in i-- order
                    if matrix[i, location_y] != "_" or i == 0:  # makes sure a current ship isn't floating here
                        return False  # a ship cannot be inserted here
                    else:
                        return True  # a ship can be inserted
            else:
                return False  # a ship cannot be inserted

            if left_right_up_down == "Up":  # checks if the ship is being located up from the initial matrix location
                if location_y != 0 and (
                        location_y - 1) >= ship_length:  # checks that the ship doesn't fall on the unallowed boarder and the the initial length is OK
                    for i in reversed(range(location_y, 0)):  # loops from initial array location in i-- order
                        if matrix[location_x, i] != "_" or i == 0:  # makes sure a ship is not here
                            return False  # ship is not allowed to be inserted
                        else:
                            return True  # a ship is allowed here
                else:
                    return False  # a ship is not allowed here

                if left_right_up_down == "Down":  # checks for a ship to be inserted down from the initial matrix location
                    if location_y != 0 and (
                            location_y - 1) >= ship_length:  # checks to make sure the ship will fit in this location and that it doesn't fall on the boarder
                        for i in range(location_y, 0):  # loops in to see if a ship is already here
                            if matrix[location_x, i] != "_" or i == 0:
                                return False  # ship cannot be inserted
                    return True  # a ship can be inserted
                else:
                    return False  # a ship cannot be inserted

    # method to insert ships into board


def insert_ships(self, ship, direction, left_or_right, location_x, location_y):
    # checks if insertion is for horizontal
    if direction == "horizontal":
        direction_for_ship = 1
        ship_length = get_ship_length(self, ship)
        if left_or_right == "Right":


def check_if_hit(x, y):  # Checks with with values in matrix to change board.
    if matrix[x][y] == 'C' or matrix[x][y] == 'B' or matrix[x][y] == 'R' or matrix[x][y] == 'S' or \
            matrix[x][y] == 'D' \
            or matrix[x][y] == 'D':  # checks what kind of ship is hit.
        matrix[x][y] = 'X'  # X is for hit on game board.
        return True
    else:
        matrix[x][y] = '0'  # 0 is miss on game board.
        return False


pass
