import sys

length, width = 12, 11
side = 'ABCDEFGHIJ'
empty = ' _ _ _ _ _ _ _ _ _ _ _ _'
matrix = [[0 for x in range(width)] for y in range(length)]


def layout_board():
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


def 

layout_board()
print_ownboard()
