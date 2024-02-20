from numpy import double

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
            # return f"{self.User.username} posted a product for sale:\nFor sale! {self.item}, price: {self.price}, pickup from: {self.location}\n"
            print(
                f"{self.User.username} posted a product for sale:\nFor sale! {self.item}, price: {self.price}, pickup from: {self.location}\n")
            return f"{self.User.username} posted a product for sale:\nFor sale! {self.item}, price: {self.price}, pickup from: {self.location}\n"

        else:
            # return f"{self.User.username} posted a product for sale:\nSold! {self.item}, price: {self.price}, pickup from: {self.location}\n"

            print(
                f"{self.User.username} posted a product for sale:\nSold! {self.item}, price: {self.price}, pickup from: {self.location}\n")
            return f"{self.User.username} posted a product for sale:\nSold! {self.item}, price: {self.price}, pickup from: {self.location}\n"

        pass

    def sold(self, password):
        if password == self.User.password:
            self.valid = False
            print(f"{self.User.username}'s product is sold")

    def discount(self, discount: str, password):
        if password == self.User.get_Password():
            if self.valid == True:
                number_discount = int(discount)
                x = 100 - number_discount
                x = x / 100
                self.price = double(self.price * x)
                # Discount on Charlie product! the new price is: 37800.0
                print("Discount on", self.User.get_username(), "product! the new price is", self.price)
