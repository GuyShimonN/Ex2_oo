from post import post


class TextPost(post):
    def __init__(self,user,*args):
        super().__init__(user)
        self.text =args[0][0]
        print( f"{self.User.username} publish  a post {self.text}\n")


    def __str__(self):
        return f"{self.User.username} publish  a post {self.text}\n"
