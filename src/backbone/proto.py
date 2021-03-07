
def proto_parse(string: bytes, is_received: bool = False):
    if not type(string) is str:
        string = string.decode('utf-8')
    try:
        if not ':' in string:
            code = 'MS'
        else:
            code, string = string.split(':')
        responce = codes[code](string, is_received)
    except KeyError as err:
        responce = str(err)
        code = 'ER'
    except ValueError:
        responce = str(err)
        code = 'ER'

    packed_responce = proto_pack(responce, code, is_received).encode('utf-8')
    return(packed_responce)

def proto_pack(responce: str, code: str, received: bool):
    if received:
        return(f'{responce}')
    return(f'{code}:{responce}')
        

def error(string: str, received: bool = False):
    pass

def heartbeat(string: str, received: bool = False):
    pass

def chatpool(string: str, received: bool = False):
    pass

def update(string: str, received: bool = False):
    pass

def whisper(string: str, received: bool = False):
    pass

def message(string: str, received: bool = False):
    return(string)

def user_login(string: str, received: bool = False):
    pass

def user_logout(string: str, received: bool = False):
    pass

def ping(string: str, received: bool = False):
    return(string)

codes = {'HB': heartbeat,
         'CP': chatpool,
         'UD': update,
         'PM': whisper,
         'MS': message,
         'PG': ping,
         'LI': user_login,
         'LO': user_logout,
         'ER': error}