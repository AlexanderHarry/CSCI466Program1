import sys
from random import randint, random

length, width = 12, 12
side = 'ABCDEFGHIJ'
matrix = [[0 for x in range(width)] for y in range(length)]
ship_vert_hor_top = ["Horizontal", "Vertical"]
ship_right_left_down_up_top = ["Right", "Left", "Up", "Down"]
ship_vert_hor_size = len(ship_vert_hor_top) - 1
ship_direction_size = len(ship_right_left_down_up_top) - 1


class BoardManager(object):

    def start_board(self):
        for i in range(0, width - 1):
            for j in range(0, length - 1):
                if j == 0 and i > 0:
                    matrix[i][j] = side[i - 1]
                elif i == 0 and j > 0:
                    matrix[i][j] = j
                elif i == 0 and j == 0:
                    matrix[i][j] = ' '
                else:
                    matrix[i][j] = '_'
                pass

    def print_board(self):
        sys.stdout = open('own_board.txt', 'w')
        for i in range(0, width - 1):
            for j in range(0, length - 1):
                print(matrix[i][j], end=" ")
            print()

    pass

    def convert_user_input(x, y):
        if x.isalpha():
            found = False
            while not found:
                for i in side:
                    if x == side[i]:
                        new_x = i
                        found = True
                    else:
                        found = False
        else:
            print('coordinate X invalid')
        if not y.isint():
            print('coordinate Y invalid')
        else:
            hit = check_if_hit(new_x, y)
        return hit

    pass

    # method to get random selections for the ship insert
    def get_insert_info(self, ship_list):
        # gets the length of the lists
        ship_list_size = len(ship_list) - 1
        # chooses what list value will be randomly selected
        ship_to_insert = randint(0, ship_list_size)

        ship_vert_hor_descision = randint(0, ship_vert_hor_size)
        if ship_vert_hor_top[ship_vert_hor_descision] == "Vertical":
            ship_direction_descision = randint(2, 3)


        else:
            ship_direction_descision = randint(0, 1)

        # chooses random coordinates
        x = randint(1, width - 1)
        y = randint(1, length - 1)
        # returns ship variables in a list of ints
        return [ship_to_insert, ship_vert_hor_descision, ship_direction_descision, x, y]
        pass

    def check_fit(self, ship_insert_info, ship_string_list):
        counter = 0
        ship = ship_string_list[ship_insert_info[0]]
        # if statement to set ship length

        if ship == 'Carrier':
            ship_length = 5
        elif ship == 'Battleship':
            ship_length = 4
        elif ship == 'Cruiser' or ship == "Submarine":
            ship_length = 3
        elif ship == 'Destroyer':
            ship_length = 2
        else:
            ship_length = sys.maxint
        direction = ship_vert_hor_top[ship_insert_info[1]]
        left_right_up_down = ship_right_left_down_up_top[ship_insert_info[2]]
        location_x = ship_insert_info[3]
        location_y = ship_insert_info[4]

        if direction == "Horizontal":  # Checks if the ship is going to be inserted horizontally
            # checks to see if the ship is being inserted to the right of the
            # initial location
            if left_right_up_down == "Right":

                if (width - 1) - location_x >= ship_length and location_x != 0:
                    # checks that the ship falls in
                    # the board and will fit

                    # loops to make sure the ship wont interfere with a ship already on the
                    for i in range(location_x, location_x + ship_length - 1, 1):
                        if counter == ship_length: break
                        counter += 1
                        # board
                        if matrix[i][location_y] != '_' or location_x + ship_length > 11:
                            return False  # returns a false that the ship cannot be inserted
                    if counter == ship_length:
                        return True  # returns true if the ship can be inserted
                else:
                    return False  # returns a false that the ship cannot be inserted
            if left_right_up_down == "Left":  # checks that the shift is being placed to the left of the initial peg
                # checks that the ship falls in the board and
                # will fit
                if location_x >= ship_length and location_x != 0:
                    # checks to make sure the ship will fit.  loops in i-- order
                    for i in range(location_x, location_x - ship_length - 1, -1):
                        if counter == ship_length: break
                        counter += 1
                        if matrix[i][
                            location_y] != '_':  # makes sure a current ship isn't floating here
                            return False  # a ship cannot be inserted here
                    if counter == ship_length:
                        return True  # a ship can be inserted
                else:
                    return False  # a ship cannot be inserted
        if direction == "Vertical":
            if left_right_up_down == "Up":  # checks if the ship is being located up from the initial matrix location
                if location_y != 0 and location_y >= ship_length:

                    # checks that the ship doesn't fall on the unallowed boarder
                    #  and the the initial length is OK
                    # loops from initial array location in i-- order

                    for i in range(location_y, location_y - ship_length + 1, - 1):
                        if counter == ship_length: break
                        # makes sure a ship is not here
                        counter += 1
                        if matrix[location_x][i] != '_':
                            return False  # ship is not allowed to be inserted
                    if counter == ship_length:
                        return True  # a ship is allowed here
                else:
                    return False  # a ship is not allowed here

            if left_right_up_down == "Down":  # checks for a ship to be inserted down from the initial matrix
                # location
                # checks to make sure the ship will fit in this location
                if location_y != 0 and (length - location_y + 1) >= ship_length:
                    #  and that it doesn't fall on the boarder
                    for i in range(location_y, location_y + ship_length - 1, 1):  # loops in to see if a ship is already here
                        if counter == ship_length: break
                        counter += 1
                        if matrix[location_x][i] != '_':
                            return False  # ship cannot be inserted
                if counter == ship_length:
                    return True  # a ship can be inserted
            else:
                return False  # a ship cannot be inserted

        pass

    def insert_ship(self, ship, ship_char, ship_length):
        # checks if ship is vertical
        ship_vertical_hor = ship_vert_hor_top[ship[1]]
        ship_up_down_left_right = ship_right_left_down_up_top[ship[2]]
        x = ship[3]
        y = ship[4]

        if ship_vertical_hor == 'Vertical':
            if ship_up_down_left_right == 'Up':
                for i in range(y, y - ship_length, -1):
                    matrix[x][i] = ship_char
            elif ship_up_down_left_right == 'Down':
                for i in range(y, y + ship_length - 1, 1):
                    matrix[x][i] = ship_char
        elif ship_vertical_hor == 'Horizontal':
            if ship_up_down_left_right == 'Right':
                for i in range(x, x + ship_length - 1, 1):
                    matrix[i][y] = ship_char
            elif ship_up_down_left_right == 'Left':
                for i in range(x, x - ship_length - 1, - 1):
                    matrix[i][y] = ship_char

        pass

    def get_char(self, ship):
        if ship == 0:
            # returns C for Carrier
            return 'C'
        elif ship == 1:
            # returns B for Battleship
            return 'B'
        elif ship == 2:
            # returns R for Cruiser
            return 'R'
        elif ship == 3:
            # returns S for Submarine
            return 'S'
        elif ship == 4:
            # returns D for Destroyer
            return 'D'
        # returns Water
        else:
            return '_'

        pass

    def get_ship_length(self, ship):
               # gets Carrier size
        if ship == 0:
            return 5
        # gets Battleship size
        elif ship == 1:
            return 4
        # returns size for cruiser or submarine
        elif ship == 2 or ship == 3:
            return 3
        # returns size for destroyer
        elif ship == 4:
            return 2
        else:
            return 9999
        pass


def check_if_hit(x, y):
    if matrix[x][y] == 'C' or matrix[x][y] == 'B' or matrix[x][y] == 'R' or matrix[x][y] == 'S' or matrix[x][y] == 'D' \
            or matrix[x][y] == 'D':
        matrix[x][y] = 'X'
        return True
    else:
        matrix[x][y] = '0'
        return False


pass
