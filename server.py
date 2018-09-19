import socket
# sets the buffer size
buffer_size = 1024
# creating a server
my_socket = socket.socket(socket.AF_INet, socket.SOCK_STREAM)
# binds to an address and port
my_socket.bind(('0.0.0.0', 5000))
# allows 1 connection
my_socket.listen(1)

# createing the client side
my_socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connects to the ip and port
my_socket.connect((LOCAL_HOST,5000))
# sends the bytes
my_socket.send(bytes('POST...'))
# receives the data
data = my_socket.recv(buffer_size)
# closes the connection
my_socket.close()

# creating a new socket for the server
connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# binding a new socket
connection.bind((LOCAL_HOST, 5000))
# setting amount of connections
connection.listen(1)
# server connect creates a new socket
connection.addr = my_socket.accept()
# receives the data
data = connection.recv(buffer_size)
# sends the data
connection.send(data)
# closes the connection
connection.close()