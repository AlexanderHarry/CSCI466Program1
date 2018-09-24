import sys
from random import randint, random

length, width = 12, 12
side = 'ABCDEFGHIJ'
matrix = [[0 for x in range(width)] for y in range(length)]
opponentBoard = [[0 for x in range(width)] for y in range(length)]
ship_vert_hor_top = ["Horizontal", "Vertical"]
ship_right_left_down_up_top = ["Right", "Left", "Up", "Down"]
ship_vert_hor_size = len(ship_vert_hor_top) - 1
ship_direction_size = len(ship_right_left_down_up_top) - 1
my_carrier_count = ['C', 'C', 'C', 'C', 'C']
my_battleship_count = ['B', 'B', 'B', 'B']
my_sub_count = ['S', 'S', 'S']
my_cruiser_count = ['R', 'R', 'R']
my_destroyer_count = ['D', "D"]
opponents_ships_sunk = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer", "Destroyer"]



def check_if_sunk(ship):
    if not ship:
        return True
    else:
        return False
    pass


class BoardManager(object):

    def start_board(self):
        for i in range(0, width - 1):
            for j in range(0, length - 1):
                if j == 0 and i > 0:
                    matrix[i][j] = side[i - 1]
                    opponentBoard[i][j] = side[i - 1]
                elif i == 0 and j > 0:
                    matrix[i][j] = j
                    opponentBoard[i][j] = j
                elif i == 0 and j == 0:
                    matrix[i][j] = ' '
                    opponentBoard[i][j] = ' '
                else:
                    matrix[i][j] = '_'
                    opponentBoard[i][j] = '_'
                pass

    def print_board(self):
        sys.stdout = open('own_board.txt', 'w')
        for i in range(0, width - 1):
            for j in range(0, length - 1):
                print(matrix[i][j], end=" ")
            print()
        sys.stdout = open('opponent_board.txt', 'w')
        for i in range(0, width - 1):
            for j in range(0, length - 1):
                print(opponentBoard[i][j], end=" ")

            print()

    pass

    # method to get random selections for the ship insert
    def get_insert_info(self, ship_list):
        # gets the length of the lists
        ship_list_size = len(ship_list) - 1
        # chooses what list value will be randomly selected
        ship_to_insert = randint(0, ship_list_size)
        # selects random horizontal or vertical
        ship_vert_hor_descision = randint(0, ship_vert_hor_size)
        # if statements to match and set board
        if ship_vert_hor_top[ship_vert_hor_descision] == "Vertical":
            # sets up players direction, up,down
            ship_direction_descision = randint(2, 3)

        else:
            # sets up players direction, left,right
            ship_direction_descision = randint(0, 1)

        # chooses random coordinates
        x = randint(1, width - 2)
        y = randint(1, length - 2)
        # returns ship variables in a list of ints
        return [ship_to_insert, ship_vert_hor_descision, ship_direction_descision, x, y]
        pass

    # method to check if the ship fits, if it does it is inserted into the board
    def check_fit(self, ship_insert_info, ship_string_list):
        counter = 0
        # gets ships name
        ship = ship_string_list[ship_insert_info[0]]
        # gets ships character value and length
        character, ship_length = self.get_char(ship)
        # gets if ship is horizontal or vertical
        direction = ship_vert_hor_top[ship_insert_info[1]]
        # gets if ship is left or right
        left_right_up_down = ship_right_left_down_up_top[ship_insert_info[2]]
        # x and y are the starting variables to insert into matrix
        x = ship_insert_info[3]
        y = ship_insert_info[4]

        if direction == "Horizontal":  # Checks if the ship is going to be inserted horizontally
            # checks to see if the ship is being inserted to the right of the
            # initial location
            if left_right_up_down == "Right":
                # checks that the ship falls in the board and will fit
                if (width - 1) - x >= ship_length and x != 0:

                    # loops to make sure the ship wont interfere with a ship already on the
                    for i in range(x, x + ship_length, 1):

                        if counter == ship_length: break
                        counter += 1
                        # board
                        if matrix[y][i] != '_' or x + ship_length > 11:
                            return False  # returns a false that the ship cannot be inserted
                    if counter == ship_length:
                        counter = 0
                        # inserts the ships into the board
                        for i in range(x, x + ship_length, 1):
                            if counter == ship_length: break
                            counter += 1
                            matrix[y][i] = character
                        return True  # returns true if the ship can be inserted
                else:
                    return False  # returns a false that the ship cannot be inserted
            elif left_right_up_down == "Left":  # checks that the shift is being placed to the left of the initial peg
                # checks that the ship falls in the board and
                # will fit
                if x >= ship_length and x != 0:
                    # checks to make sure the ship will fit.  loops in i-- order
                    for i in range(x, x - ship_length - 1, -1):
                        if counter == ship_length: break
                        counter += 1
                        # makes sure a current ship isn't floating here
                        if matrix[y][i] != '_':
                            return False  # a ship cannot be inserted here
                    if counter == ship_length:
                        counter = 0
                        # inserts the ships into the board
                        for i in range(x, x - ship_length - 1, -1):
                            if counter == ship_length: break
                            counter += 1
                            matrix[y][i] = character
                        return True  # returns true if the ship can be inserted
                else:
                    return False  # a ship cannot be inserted
        if direction == "Vertical":
            if left_right_up_down == "Up":  # checks if the ship is being located up from the initial matrix location
                if y != 0 and y >= ship_length:

                    # checks that the ship doesn't fall on the unallowed boarder
                    #  and the the initial length is OK
                    # loops from initial array location in i-- order

                    for i in range(y, y - ship_length, - 1):
                        if counter == ship_length: break
                        # makes sure a ship is not here
                        counter += 1
                        if matrix[i][x] != '_':
                            return False  # ship is not allowed to be inserted
                    if counter == ship_length:
                        counter = 0
                        # inserts the ships into the board
                        for i in range(y, y - ship_length, -1):
                            if counter == ship_length: break
                            counter += 1
                            matrix[i][x] = character
                        return True  # returns true if the ship can be inserted
                else:
                    return False  # a ship is not allowed here

            elif left_right_up_down == "Down":  # checks for a ship to be inserted down from the initial matrix
                # location
                # checks to make sure the ship will fit in this location
                if y != 0 and (length - y + 1) >= ship_length:
                    #  and that it doesn't fall on the boarder
                    for i in range(y, y + ship_length + 1, 1):  # loops in to see if a ship is already here
                        if counter == ship_length or i > 11: break
                        counter += 1
                        if matrix[i][x] != '_':
                            return False  # ship cannot be inserted
                if counter == ship_length:
                    counter = 0
                    # inserts the ships into the board
                    for i in range(y, y + ship_length + 1, 1):
                        if counter == ship_length: break
                        counter += 1
                        matrix[i][x] = character
                    return True  # returns true if the ship can be inserted
                else:
                    return False  # a ship cannot be inserted

        pass

    # method to get the character value of the ship
    def get_char(self, ship):

        if ship == "Carrier":
            # returns C and ship size for Carrier
            return 'C', 5
        elif ship == "Battleship":
            # returns B  and ship size for Battleship
            return 'B', 4
        elif ship == "Cruiser":
            # returns R and ship size for Cruiser
            return 'R', 3
        elif ship == "Submarine":
            # returns S and ship size for Submarine
            return 'S', 3
        elif ship == "Destroyer":
            # returns D and ship size for Destroyer
            return 'D', 1
        # returns Water
        else:
            return '_'

        pass

    def check_if_hit(self, x, y):

        ship_sunk = False
        if matrix[y][x] == 'C':
            my_carrier_count.pop(0)
            matrix[y][x] = 'X'
            opponentBoard[y][x] = 'X'
            sunk = check_if_sunk(my_carrier_count)
            if sunk:
                opponents_ships_sunk.remove('Carrier')
            return True, "hit", sunk, "Carrier"
        elif matrix[y][x] == 'B':
            my_battleship_count.pop(0)
            matrix[y][x] = 'X'
            opponentBoard[y][x] = 'X'
            sunk = check_if_sunk(my_battleship_count)
            if sunk:
                opponents_ships_sunk.remove("Battleship")
            return True, "hit", sunk, "Battleship"
        elif matrix[y][x] == 'R':
            my_cruiser_count.pop(0)
            matrix[y][x] = 'X'
            opponentBoard[y][x] = 'X'
            sunk = check_if_sunk(my_cruiser_count)
            if sunk:
                opponents_ships_sunk.remove("Cruiser")
            return True, "hit", sunk, "Cruiser"
        elif matrix[y][x] == 'S':
            my_sub_count.pop(0)
            matrix[y][x] = 'X'
            opponentBoard[y][x] = 'X'
            sunk = check_if_sunk(my_sub_count)
            if sunk:
                opponents_ships_sunk.remove("Submarine")
            return True, "hit", sunk, "Submarine"
        elif matrix[y][x] == 'D':
            my_destroyer_count.pop(0)
            matrix[y][x] = 'X'
            opponentBoard[y][x] = 'X'
            sunk = True
            opponents_ships_sunk.remove("Destroyer")
            return True, "hit", sunk, "Destroyer"

        elif matrix[y][x] == '_':
            opponentBoard[y][x] = '.'

            return False, "not hit", False, "no Ship"
        return False, "not hit", False, "no Ship"

        pass

    def game_still_goint(self):
        if opponents_ships_sunk == []:
            return False
        else: return True
        pass


