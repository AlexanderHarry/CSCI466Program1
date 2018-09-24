import socket
import http.client
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from random import randint, random
import re

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


def print_board(in_board):
    # if in_board == own_board:
    #     sys.stdout = open('own_board.txt', 'w')
    # elif in_board == opponents_board:
    #     sys.stdout = open('opponent_board.txt', 'w')
    for i in range(0, width - 1):
        for j in range(0, length - 1):
            print(in_board[i][j], end=" ")
        print()


def validate_coordinates(x, y):
    if x < 1 or x > 9 or y > 9 or y < 1:
        return [404, "HTTP NOT_FOUND"]
    elif own_board[x][y] == 'X' or own_board[x][y] == '0':
        return [410, "HTTP GONE"]
    else:
        return check_if_hit(x, y)


def check_if_hit(x, y):  # MAY have to update to file. Check if sunk and return hit=1 or hit=0
    if own_board[x][y] == 'C' or own_board[x][y] == 'B' or own_board[x][y] == 'R' or own_board[x][y] == 'S' or \
            own_board[x][y] == 'D' \
            or own_board[x][y] == 'D':
        own_board[x][y] = 'X'
        # update board maybe
        http_value = 200
        message = 'hit=1'
        # check if sunk, if sunk message = hit=1&sink=...
    else:
        own_board[x][y] = '_'
        http_value = 200
        message = 'hit=0'
    return [http_value, message]


class Server(BaseHTTPRequestHandler):  # Used to implement servers.

    def get_handler(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if self.path == '/own_board.html':  # if path in the HTTP message is the own_board, request is for own_board.
            print_board(own_board)
            board_file = open('own_board.txt', 'r')
            self.wfile.write(('<html><body><h1><pre>' + board_file.read() + '</pre></h1></body></html>').encode())S

        elif self.path == '/opponent_board.txt':  # if the path in the HTTP message is the opponent_board.
            print_board(opponents_board)


    # must create format for message and send using self.wfile.write(file.encode)

    def post_handler(self, data):
        match = re.search("x=\d&y=\d", data)
        if match:
            x = match.group(1)
            y = match.group(2)
        else:
            return [404, "HTTP GONE"]  # NOT FOUND
        message = validate_coordinates(x, y)
        self.send_response(message[0])
        self.send_header('Content-Type', 'text')
        self.end_headers()
        self.wfile.write(message[1].encode())  # Send Html message


    def main(self):
        file = open(sys.argv[2])  # will use to print board
        port = int(sys.argv[1])  # will use to get socket

        start_boards()
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', port))
        s.listen(1)
        conn, addr = s.accept()
        data = conn.recv(1024)
        print("Received Request: '" + data.decode('utf-8') + "'")
        conn.send('Yes'.encode('utf-8'))
