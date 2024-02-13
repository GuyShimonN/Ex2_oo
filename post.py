from abc import ABC, abstractmethod

class post(ABC):


    def __init__(self,User):
      self.how_like=[]

      self.User =User



    def like(self,user):
        if (user not in self.how_like):
            self.how_like.append(user)
            user.notifications


    def unlike(self,user):
        if (user in self.how_like):
            self.how_like.remove(user)

    def comment(self,user,comment):
        pass

    @abstractmethod
    def __str__(self):
        pass

