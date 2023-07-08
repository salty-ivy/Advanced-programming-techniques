class SensitiveInfo:
    def __init__(self):
        self.users = ['aman', 'ojas', 'laki']

    def read(self):
        nb = len(self.users)
        print(self.users, nb)

    def add(self, user):
        self.users.append(user)
        print("added", self.users)


class Info:
    '''protection proxy to SensitiveInfo'''
    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = '0xdeadbeef'

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input('what is the secret? ')
        self.protected.add(user) if sec == self.secret else print("That's wrong!")