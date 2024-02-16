from abc import ABC, abstractmethod

class post(ABC):
    def __init__(self,User):
      self.how_like=set()
      self.User =User
      self.comments= []

    def like(self,user):
        #use set beacuse i want to prevent duplicate like
        self.how_like.add(user)
        print(f"notification to {self.User.get_username()}: {user.username} liked your post")




    def unlike(self,user):
        #use set beacuse i want to prevent duplicate like
        self.how_like.remove(user)

    def comment(self,user,comment):
        #use at dictonrt the key: user value:comment
            self.comments.append(user)
            self.User.notifications.append(f"{user.username} commendet on your post")


    @abstractmethod
    def __str__(self):
        pass

