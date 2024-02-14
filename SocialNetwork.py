from User import User





class SocialNetwork:

    def __init__(self, name):
        self.social_network = name
        print(f"The social network {name} was created!")
        self.accounts = {}

    def sign_up(self, username, password):
        if (username in self.accounts) | (len(password) < 4) | (len(password) > 8):
            print("is not vallid try again")
        else:
            a = User(username, password)
            self.accounts[username] = a
            print(f"The social network {username} and {password} was created!")
            return a

    def get_social_network(self):
        return self.social_network

    def log_in(self, username: str, password):
        if username in self.accounts:
            user = self.accounts.get(username)
            if password == user.password:
                user.set_concted(True)
                print(f" {user.username}is conected to the social")
            else:
                print("the password is incorrect ")
        else:
            print("the acouunt not exsit")

    def log_out(self, username: str):
        if username in self.accounts:
            print(username)
            user = self.accounts.get(username)
            user.set_concted(False)
            print(f" {user.username} disconnected from the social")

    def print(self):
        print(f"The social network : {self.social_network}was created!")

