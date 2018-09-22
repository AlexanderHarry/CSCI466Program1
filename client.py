import socket

# creating the client side
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connects to the ip and port
s.connect(('localhost', 80))
# sends the bytes
s.send(bytes('POST...'))
# receives the data
data = s.recv(1024)
# closes the connection
s.close()