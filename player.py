# from doctest import master
# import tkinter
# from random import randint

from board_manager import BoardManager
from tkinter import *

# lists of ships for the game
ship_list = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer", "Destroyer"]
ship_direction = ["Horizontal", "Vertical"]
ship_right_left_down_up = ["Right", "Left", "Up", "Down"]
ship_descending_list = ship_list  # temp variable to pass in to add ships to
x_choice = 'Y'
y_choice = 23
shots_fired = []


#  playerServer = Server()

# from server import Server
def set_up_player_board(board):
    # starts board
    board.start_board()
    # loops untill all the ships are inserted
    while ship_descending_list:
        # returns list for ship to be inserted [name, direction, up, x, y] just int values
        ship_insert_info = board.get_insert_info(ship_descending_list)
        # checks that the location works and inserts if true
        location_ok = board.check_fit(ship_insert_info, ship_descending_list)
        if location_ok:
            # removes the ship from the list, keeps track of game pieces placed on start up
            ship_descending_list.remove(ship_list[ship_insert_info[0]])
    pass


def fire():
    # shot_fired = False
    # while shot_fired == False:
    #     x = randint(1, 10)
    #     y = randint(1, 10)
    #     if [x, y] not in shots_fired:
    #         board.shoot_at(x, y)
    #         shot_fired = True
    sys.stdout = open('test.txt', 'w')
    print("test")


print()
pass


def chooseMove(board):
    popup = Tk()
    fire_button = Button(popup, text="Fire!", command=fire)
    fire_button.pack(fill=X)
    popup.mainloop()
    pass


class Player():
    # lists of ships for the game
    ship_list = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer", "Destroyer"]
    ship_direction = ["Horizontal", "Vertical"]
    ship_right_left_down_up = ["Right", "Left", "Up", "Down"]
    ship_descending_list = ship_list  # temp variable to pass in to add ships to
    #  playerServer = Server()
    board = BoardManager()
    # set up player board
    set_up_player_board(board)
    board.print_board()
    chooseMove(board)
    board.print_board()
