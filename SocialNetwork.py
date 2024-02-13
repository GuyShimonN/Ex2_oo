class SocialNetwork:
    accounts = {}

    def __init__(self, name):
        self.social_network = name

    def sign_up(self, username, password):
        pass

    def get_social_network(self):
        return self.social_network

    def log_in(self, username, password):
        # if username in self.accounts:
        #     self.accounts[]
        #     return True
        pass

    def log_out(self, username):
        # if username in self.accounts:
        #     del self.accounts[username]
        #     return True
        pass

    def print(self):
        print(f"The social network : {self.social_network}was created!")

    pass
