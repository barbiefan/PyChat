import socket
from _thread import start_new_thread
import proto
import time

class Client():

    t1 = 0
    t2 = 0

    def __init__(self, IP, PORT, buffer_size=2048):
        self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.BUFFER_SIZE = buffer_size
        if IP and PORT:
            self.connect(IP, PORT)

    def connect(self, IP, PORT):
        try:
            print(f'Connecting to Server {IP}:{PORT}')
            self.Socket.connect((IP, PORT))
            print('done.')
            start_new_thread(self.listen_deamon, tuple())
            start_new_thread(self.send_deamon, tuple())
        except Exception as err:
            print('CONNECTION ERROR:')
            print(str(err))

    def listen_deamon(self):
        print('Started listening deamon')
        try:
            while True:
                msg = self.Socket.recv(self.BUFFER_SIZE)
                parsed_msg = proto.proto_parse(msg)
                """
                if data.startswith('PG'):
                    self.t2 = time.perf_counter()
                if self.t1 != 0 and self.t2 != 0:
                    data = f'ping is: {self.t2-self.t1}, echo: {data}'
                    self.t1 = 0
                    self.t2 = 0
                """
                print(f'\n{parsed_msg.decode("utf-8")}')
        except Exception as err:
            print('RECEIVING ERROR:')
            print(str(err))
            print('disconnecting...')
            self.Socket.close()
            print('done.')

    def send_deamon(self):
        print('Started sending deamon')
        try:
            while True:
                msg = input('you: ')
                if msg == '!exit':
                    break
                parsed_msg = proto.proto_parse(msg)
                """
                if msg.startswith('PG'):
                    self.t1 = time.perf_counter()
                """
                self.Socket.send(parsed_msg)
        except Exception as err:
            print('SENDING ERROR:')
            print(str(err))
            print('disconnecting...')
            self.Socket.close()
            print('done.')

cli = Client('127.0.0.1', 5005)
time.sleep(10000)