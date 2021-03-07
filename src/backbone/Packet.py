import datetime
import json
import time

test_string = '{"Sender": "Xxx_Pussy_destroyer_xxX", "DateTimeReceived": "08.03.2021 18:02:33", "PacketCode": "MS", "Content": "test message for parsing"}'
json = json.loads(test_string)


class Packet():
    def __init__(self, string: str):
        self.sender = json["Sender"]
        if json["DateTimeReceived"] == "":
            self.datetime = str(time.time())
        else:
            self.datetime = json["DateTimeReceived"]
        self.packetcode = json["PacketCode"]
        self.content = json["Content"]
        

packet = Packet(json)
