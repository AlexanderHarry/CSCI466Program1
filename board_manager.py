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


def does_ship_fit(self, ship, direction, left_right_up_down, location_x, location_y):
    ship_length = get_ship_length(self, ship)
    if direction == "horizontal":

        if left_right_up_down == "Right":
            if (width - 1) - location_x >= ship_length and location_x != 0:
                for i in range(location_x, width):
                    if matrix[i, location_y] != "_":
                        return False
                else:
                    return True
            else:
                return False
        if left_right_up_down == "Left":
            if location_x - 1 >= ship_length and location_x != 0:
                for i in reversed(range(location_x, 0)):
                    if matrix[i, location_y] != "_" or i == 0:
                        return False
                    else:
                        return True
            else:
                return False

            if left_right_up_down == "Up":
                if location_y != 0 and (location_y - 1) >= ship_length:
                    for i in reversed(range(location_y, 0)):
                        if matrix[location_x, i] != "_" or i == 0:
                            return False
                        else:
                            return True
                else:
                    return False

                if left_right_up_down == "Down":
                    if location_y != 0 and (location_y - 1) >= ship_length:
                        for i in reversed(range(location_y, 0)):
                            if matrix[location_x, i] != "_" or i == 0:
                                return False
                    return True
                else:
                    return False

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
