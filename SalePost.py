import User
from post import post


class SalesPost(post):
    pass
    def __init__(self,username,*args):
        super().__init__(username)
        self.valid=True
        self.item=args[0]
        self.price=args[1]
        self.location=args[2]


    def __str__(self):
        pass
    def sold(self,password):
        if password==User.User.get_Password():
           self.valid=False