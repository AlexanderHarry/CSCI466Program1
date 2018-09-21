import sys

length, width = 12, 11
side = 'ABCDEFGHIJ'
matrix = [[0 for x in range(width)] for y in range(length)]


def start_board():
    for i in range(0, width - 1):
        for j in range(0, length - 1):
            if j == 0 and i > 0:
                matrix[i][j] = side[i]
            elif i == 0 and j > 0:
                matrix[i][j] = j
            elif i == 0 and j == 0:
                matrix[i][j] = ' '
            else:
                matrix[i][j] = '_'


def print_ownboard():
    sys.stdout = open('own_board.txt', 'w')
    for i in range(0, width - 1):
        for j in range(0, length - 1):
            print(matrix[i][j], end=" ")
        print()


start_board()
print_ownboard()
def update_my_board(x, y):
    if matrix[x][y] == 'C' or matrix[x][y] == 'B' or matrix[x][y] == 'R' or matrix[x][y] == 'S' or matrix[x][y] == 'D':



#
#
# def update_opponent_board()


