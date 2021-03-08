import datetime
import json
import time

test_string = '{"Sender": "Xxx_Pussy_destroyer_xxX", "DateTimeReceived": "08.03.2021 18:02:33", "PacketCode": "MS", "Content": "fuck u bitch"}'

class Packet():
    
    def __init__(self, string: str):
        slovar = json.loads(string)
        self.Sender = slovar["Sender"]
        if slovar["DateTimeReceived"] == "":
            self.DateTime = str(time.time())
        else:
            self.DateTime = slovar["DateTimeReceived"]
        self.PacketCode = slovar["PacketCode"]
        self.Content = slovar["Content"]
    
    def to_json(self):
        attributes = {
            'Sender': self.Sender,
            'DateTime': self.DateTime,
            'PacketCode': self.PacketCode,
            'Content': self.Content 
            }
        return json.dumps(attributes)
        

packet = Packet(test_string)