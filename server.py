import socket;
buffer_size = null
#creating a server
my_socket = socket.socket(socket.AF_INet, socket.SOCK_STREAM)
my_socket.bind(('0.0.0.0', 5000))
my_socket.listen(1)

# createing the client side
my_socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('0.0.0.0',5000))
my_socket.send(bytes('POST...'))
data = my_socket.recv(buffer_size)
my_socket.close()

#server connect creates a new socket
conn.addr = my_socket.accept()
data = conn.recv(buffer_size)
conn.send(data)
conn.close()