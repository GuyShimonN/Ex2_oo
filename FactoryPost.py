import post
import TextPost
import SalePost
import ImagePost


class FactoryPost:
    def __init__(self,username,type:str,*args):
        self.type = type
        if(self.type == "Text"):

            pass
        if(self.type == "Image"):
            pass
        if(self.type == "Sale"):
            pass