
def proto_parse(string: bytes):
    if not type(string) is str:
        string = string.decode('utf-8')
    try:
        code, string = string.split(':')
        responce = codes[code](string)
    except KeyError as err:
        responce = str(err)
        code = 'ER'
    except ValueError:
        responce = str(err)
        code = 'ER'

    packed_responce = proto_pack(responce, code)
    return(packed_responce)

def proto_pack(responce: str, code: str):
    return(f'{code}:{responce}')

def error(string: str):
    pass

def heartbeat(string: str):
    pass

def chatpool(string: str):
    pass

def update(string: str):
    pass

def whisper(string: str):
    pass

def ping(string: str):
    return(string)

codes = {'HB': heartbeat,
         'CP': chatpool,
         'UD': update,
         'PM': whisper,
         'PG': ping,
         'ER': error}