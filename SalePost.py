import User
from post import post


class SalesPost(post):

    def __init__(self, username, *args):
        super().__init__(username)
        self.valid = True
        self.item = args[0][0]
        self.price = args[0][1]
        self.location = args[0][2]
        print(
            f"{self.User.username} posted a product for sale:\nFor sale! {self.item}, price: {self.price}, pickup from: {self.location}\n")

    def __str__(self):
        if self.valid:
            print(
                f"{self.User.username} posted a product for sale:\nFor sale! {self.item}, price: {self.price}, pickup from: {self.location}\n")
        else:
            print(
                f"{self.User.username} posted a product for sale:\nSold! {self.item}, price: {self.price}, pickup from: {self.location}\n")

        pass
    def sold(self,password):
        if password==User.User.get_Password():
           self.valid=False