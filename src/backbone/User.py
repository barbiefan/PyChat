class User():
    def __init__(self, nickname: str, password_hash: str, ID="::auto::", email=None):
        self.Nickname = nickname
        self.ID = ID
        self.Email = email
        self.Password = password_hash
        self.Knonw_IPs = []

    def login(self):
        pass

    def logout(self):
        pass