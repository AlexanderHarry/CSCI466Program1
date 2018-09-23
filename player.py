from doctest import master
import tkinter
from random import randint
from board_manager import BoardManager
from tkinter import *

# lists of ships for the game
ship_list = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer", "Destroyer"]
ship_direction = ["Horizontal", "Vertical"]
ship_right_left_down_up = ["Right", "Left", "Up", "Down"]
ship_descending_list = ship_list  # temp variable to pass in to add ships to
x_choice = 'Y'
y_choice = 23
shots_fired_track = []
ships_sunk = []
board = BoardManager()


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


def rand_coordinate():
    return randint(1, 10)
    pass


def already_played(x, y):
    if [x, y] in shots_fired_track:
        return True
    else:
        return False
    pass



def fire():
    last_hit = []
    hit_ship = False
    continue_loop = True
    while len(ships_sunk) != 5:

        if not continue_loop: break
        if not hit_ship:
            x = rand_coordinate()
            y = rand_coordinate()
        if last_hit != []:
            number = last_hit.pop()
            x = number[0]
            y = number[1]
            if not already_played(x + 1, y) and x + 1 < 11:
                x += 1
            elif not already_played(x - 1, y) and x - 1 > 0:
                x -= 1
            elif not already_played(x, y + 1) and y + 1 < 11:
                y += 1
            elif not already_played(x, y - 1) and y - 1 > 0:
                y -= 1

        mark, hit_or_not, sunk, ship_name = board.check_if_hit(x, y)
        print(hit_or_not)
        shots_fired_track.append([x, y])
        if mark == True:
            hit_ship = True
            last_hit.append([x, y])

            if sunk:
                ships_sunk.append(ship_name)
                hit_ship = False
        if not mark:
            last_hit = []
            hit_ship = False
            continue_loop = False


board.print_board()

print()

pass


def chooseMove():
    fire()
    # popup = Tk()
    # fire_button = Button(popup, text="Fire!", command=fire)
    # fire_button.pack(fill=X)
    # popup.mainloop()
    # pass


class Player():
    # lists of ships for the game
    ship_list = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer", "Destroyer"]
    ship_direction = ["Horizontal", "Vertical"]
    ship_right_left_down_up = ["Right", "Left", "Up", "Down"]
    ship_descending_list = ship_list  # temp variable to pass in to add ships to
    #  playerServer = Server()
    # set up player board
    set_up_player_board(board)
    board.print_board()
    while board.game_still_goint():
        chooseMove()
    board.print_board()
