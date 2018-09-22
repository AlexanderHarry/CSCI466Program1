import sys

length, width = 12, 11
coordinate_letters = 'ABCDEFGHIJ'
matrix = [[0 for x in range(width)] for y in range(length)]


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
                    if x == coordinate_letters[i]:   # May need to adjust parameters .
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


def check_if_hit(x, y):  # Checks with with values in matrix to change board.
    if matrix[x][y] == 'C' or matrix[x][y] == 'B' or matrix[x][y] == 'R' or matrix[x][y] == 'S' or matrix[x][y] == 'D' \
            or matrix[x][y] == 'D':  # checks what kind of ship is hit.
        matrix[x][y] = 'X'  # X is for hit on game board.
        return True
    else:
        matrix[x][y] = '0'  # 0 is miss on game board.
        return False
    pass
