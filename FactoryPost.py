from TextPost import TextPost
from ImagePost import ImagePost
from SalePost import SalesPost

class FactoryPost:

    def __init__(self):
        pass


    def create_post(user, type: str, *args):
        if type == "Text":
            x = TextPost(user, args)
            return x
        if type == "Image":
            return ImagePost(user,args)
        if type == "Sale":
            return SalesPost(user, args)
