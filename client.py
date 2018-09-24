import socket

# creating the client side
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connects to a server socket
s.connect(('127.0.0.1', 80))
# send a query
s.send(bytes('Are you there?'.encode('utf-8')))
# receives a response
data = s.recv(64)
print("Received response: '"+data.decode('utf-*')+"'")

# closes the connection
s.close()
