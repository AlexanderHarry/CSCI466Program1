import socket

# creating the client side
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connects to the ip and port
s.connect(('localhost', 8080))
# sends the bytes
s.send('Fire'.encode('utf-8'))
# receives the data
data = s.recv(1024)
print('Recieved response ' + data.decode('utf-8') + "'")
# closes the connection
s.close()
