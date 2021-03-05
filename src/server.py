import socket
import os
from _thread import start_new_thread

class Server():

    def __init__(self, IP='127.0.0.1', PORT=5005, backlog=10):
        self.IP = IP
        self.PORT = PORT
        self.backlog = backlog
        self.Socket = socket.socket()
        try:
            self.Socket.bind((self.IP, self.PORT))
        except socket.error as err:
            print('INITIALIZATION ERROR:')
            print(str(err))
        else:
            print(f'Server initialized. IP:PORT - {self.IP}:{self.PORT}')
        self.msg_log = []


    def listen(self, backlog=None):
        if backlog:
            self.backlog = backlog
        try:
            self.Socket.listen(self.backlog)
            print(f'Listening on {self.IP}:{self.PORT}\nbacklog: {self.backlog}')
            while True:
                Client, address = self.Socket.accept()
                print(f'Connected to: {address[0]}:{address[1]}')
                start_new_thread(self.client_thread, (Client, ))
        except Exception as err:
            print('SERVER ERROR:')
            print(str(err))
            print('closing Socket...')
            self.Socket.close()
            print('done.')

    def client_thread(self, connection):
        client_address = connection.getpeername()
        try:
            while True:
                data = connection.recv(2048).decode('utf-8')
                self.msg_log.append(data)
                reply = f'server\'s log:\n{self.msg_log}'
                if not data:
                    break
                connection.sendall(str.encode(reply))
        except Exception as err:
            print(f'CLIENT CONNECTION ERROR ({client_address[0]}:{client_address[1]}):')
            print(str(err))
        finally:
            print(f'closing connection {client_address[0]}:{client_address[1]} ...')
            connection.close()
            print('done.')

serv = Server()
serv.listen()