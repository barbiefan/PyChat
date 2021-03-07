import datetime
import json

test_string = '{"Sender": "Xxx_Pussy_destroyer_xxX", "DateTimeReceived": "08.03.2021 18:02:33", "PacketCode": "MS", "Content": "test message for parsing"}'



class Packet():
    def __init__(self, string: str):
        pass



packet = Packet(test_string)
