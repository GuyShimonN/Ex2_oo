from post import post


class ImagePost(post):
    def __init__(self,user,*args):
        super().__init__(user)
        self.image =args

    def __str__(self):
        pass

    def display(self):
        pass