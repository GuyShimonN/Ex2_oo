from User import User


class SocialNetwork:
    _instance = None

    def __new__(cls, name):  # use singleton to prevent a creating on tow object of network
        if cls._instance is None:
            cls._instance= super(SocialNetwork, cls).__new__(cls)
        return cls._instance
    #constractor
    def __init__(self, name):
        self._social_network = name
        print(f"The social network {name} was created!")
        self.accounts = {}

    # you can sing up to the network only if the username free and your password is valid(the len between 4 to 8)
    # otherwise trwo exepstion
    def sign_up(self, username, password):
        if (username in self.accounts) | (len(password) < 4) | (len(password) > 8):
            raise ValueError("is not vallid try again")

        else:
            a = User(username, password)
            self.accounts[username] = a

            return a
    #return the name of the social network
    def get_social_network(self):
        return self._social_network

    def log_in(self, username: str, password):
        if username in self.accounts:
            user = self.accounts.get(username)
            if password == user.get_Password():
                 if self.accounts.get(username).get_concted()==True:
                     raise Exception("you are all ready connect")
                 else:
                    user.set_concted(True)
                    print(f"{user.get_username()} connected")
            else:
                print("the password is incorrect ")
        else:
            print("the acouunt not exsit")

    def log_out(self, username: str):
        if username in self.accounts:

            user = self.accounts.get(username)
            if self.accounts.get(username).get_concted() == False:
                raise Exception("you are all raedy disconnected")
            else:
             user.set_concted(False)
             print(f"{user.get_username()} disconnected")

    def __str__(self):
        p =f"{self._social_network} social network:\n"
        for key, value in self.accounts.items():
            p+=value.__str__()
            p+="\n"
        return p

