# imports the board manager class
from board_manager import BoardManager


# from server import Server

# creates the player class
class Player:
    #  playerServer = Server()
    # creates an instance of BoardManager()
    board = BoardManager()

    board.start_board()
    board.print_board()
    board.does_ship_fit("Carrier", "Horizontal", "Right", 3, 5)
    #

