import socket


class Server:
    """A class for the server"""
    pass


# sets the buffer size
buffer_size = 1024
# creating a server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# binds to an address and port
s.bind(('localhost', 5000))
# allows 1 connection
s.listen(1)

conn, addr = s.accept()

data = conn.recv(buffer_size)
print("Received request: '" + data.decode('utf-8') + "'")

conn.send('Yes'.encode('utf-8'))
conn.close()
