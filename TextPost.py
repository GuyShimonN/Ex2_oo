from post import post


class TextPost(post):
    def __init__(self,user,*args):
        super().__init__(user)
        self.text =args
    pass


    def __str__(self):
        return print(f"{super().User}published a post")