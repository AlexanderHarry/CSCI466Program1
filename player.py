from board_manager import BoardManager


# from server import Server
class Player():
    ship_list = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
    ship_direction = ["Horizontal", "Vertical"]
    ship_right_left_down_up = ["Right", "Left", "Up", "Down"]
    ship_descending_list = ship_list  # temp variable to pass in to add ships to
    #  playerServer = Server()
    board = BoardManager()
    board.start_board()
    board.print_board()
    # loops untill all the ships are inserted
    while ship_descending_list:
        # returns list for ship to be inserted [name, direction, up, x, y] just int values
        ship_insert_info = board.get_insert_info(ship_descending_list)
        location_ok = board.check_fit(ship_insert_info, ship_descending_list)
        if location_ok:
            this_ship = ship_insert_info[0]

            # pops ship from list so only proper amount of ships are inserted // creates ship to insert with string values
            ship = [ship_list[this_ship], ship_insert_info[1], ship_insert_info[2],
                    ship_insert_info[3], ship_insert_info[4]]
            # gets the ships character value to be put on board
            ship_char_val = board.get_char(this_ship)
            # runs insert ship method
            board.insert_ship(ship, ship_char_val, board.get_ship_length(this_ship))
            ship_descending_list.remove(ship_list[this_ship])
            board.print_board()
