import socket
import http.client
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from random import randint, random

length, width = 12, 12
side = 'ABCDEFGHIJ'
own_board = [[0 for x in range(width)] for y in range(length)]
opponents_board = [[0 for x in range(width)] for y in range(length)]
ship_vert_hor_top = ["Horizontal", "Vertical"]
ship_right_left_down_up_top = ["Right", "Left", "Up", "Down"]
ship_vert_hor_size = len(ship_vert_hor_top) - 1
ship_direction_size = len(ship_right_left_down_up_top) - 1


def start_boards():
    for i in range(0, width - 1):
        for j in range(0, length - 1):
            if j == 0 and i > 0:
                own_board[i][j] = side[i - 1]
                opponents_board[i][j] = side[i - 1]
            elif i == 0 and j > 0:
                own_board[i][j] = j
                opponents_board[i][j] = j
            elif i == 0 and j == 0:
                own_board[i][j] = ' '
                opponents_board[i][j] = ' '
            else:
                own_board[i][j] = '_'
                opponents_board[i][j] = '_'


class Server(BaseHTTPRequestHandler):  # Used to implement servers.

    def get_handler(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if self.path == '/own_board.html':  # if the path in the HTTP message is the own_board.
        # print own board
        elif self.path == '/opponent_board.txt':  # if the path in the HTTP message is the opponent_board.

    # print opponent_board
    # must create format for message and send using self.wfile.write(file.encode)

    def post_handler(self):

    # obtain coordinates, check coordinates (HTTP Not Found or gone[404, 410], else check board if good.)
    # validate coordinates (update current method to return 404 or 410 and to then check board is successful validation)

    def main(self):
        file = open(sys.argv[2]) # will use to print board
        port = int(sys.argv[1]) # will use to get socket

        start_boards()
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', port))
        s.listen(1)
        conn, addr = s.accept()
        data = conn.recv(1024)
        print("Received Request: '" + data.decode('utf-8') + "'")
        conn.send('Yes'.encode('utf-8'))
