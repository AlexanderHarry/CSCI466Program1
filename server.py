import socket;

#creating a server
my_socket = socket.socket(socket.AF_INet, socket.SOCK_STREAM)
my_socket.bind(('0.0.0.0', 5000))
my_socket.listen(1)

        #