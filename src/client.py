import socket

SERVER = {'IP': '127.0.0.1', 'PORT': 5005}
BUFFER_SIZE = 1024

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCKET.connect((SERVER['IP'], SERVER['PORT']))

while True:
    msg = input()
    SOCKET.send(bytes(msg, 'utf-8'))
    data = SOCKET.recv(BUFFER_SIZE)
    print(f'server\'s echo: {str(data)}')

SOCKET.close()