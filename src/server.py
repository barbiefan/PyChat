import socket
from _thread import start_new_thread
import proto

class Server():

    def __init__(self, IP='127.0.0.1', PORT=5005, backlog=10, buffer_size=2048):
        self.IP = IP
        self.PORT = PORT
        self.backlog = backlog
        self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.BUFFER_SIZE = buffer_size
        try:
            self.Socket.bind((self.IP, self.PORT))
        except socket.error as err:
            print('INITIALIZATION ERROR:')
            print(str(err))
        else:
            print(f'Server initialized. IP:PORT - {self.IP}:{self.PORT}')
        self.msg_queue = []


    def listen(self, backlog=None):
        if backlog:
            self.backlog = backlog
        try:
            self.Socket.listen(self.backlog)
            print(f'Listening on {self.IP}:{self.PORT}\nbacklog: {self.backlog}')
            while True:
                Client, address = self.Socket.accept()
                print(f'Connected to: {address[0]}:{address[1]}')
                self.client_thread(Client)
        except Exception as err:
            print('SERVER ERROR:')
            print(str(err))
            print('closing Socket...')
            self.Socket.close()
            print('done.')

    def client_thread(self, connection):
        start_new_thread(self.client_listen, (connection, ))
        start_new_thread(self.client_send, (connection, ))

    def client_listen(self, connection):
        client_address = connection.getpeername()
        try:
            while True:
                msg = connection.recv(self.BUFFER_SIZE)
                if not msg:
                    break
                parsed_msg = proto.proto_parse(msg, True)
                self.msg_queue.append(parsed_msg)
        except Exception as err:
            print(f'CLIENT LISTENING/RECEIVING ERROR ({client_address[0]}:{client_address[1]}):')
            print(str(err))
        finally:
            print(f'closing connection {client_address[0]}:{client_address[1]} ...')
            connection.close()
            print('done.')

    def client_send(self, connection):
        client_address = connection.getpeername()
        cache_msg_queue = self.msg_queue.copy()
        try:
            while True:
                if self.msg_queue > cache_msg_queue:
                    diff = len(self.msg_queue)-len(cache_msg_queue)
                    diff_to_send = self.msg_queue[-diff:]
                    for message in diff_to_send:
                        connection.sendall(message)
                    cache_msg_queue = self.msg_queue.copy()

        except Exception as err:
            print(f'CLIENT SENDING ERROR ({client_address[0]}:{client_address[1]}):')
            print(str(err))
        finally:
            print(f'closing connection {client_address[0]}:{client_address[1]} ...')
            connection.close()
            print('done.')


serv = Server()
serv.listen()
