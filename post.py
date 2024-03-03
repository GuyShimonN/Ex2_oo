from abc import ABC, abstractmethod

class post(ABC):
    def __init__(self,User):
      self.how_like=set()
      self.how_like.add(User)
      self.User =User
      self.comments= []
      self.comments.append(User)

    def like(self,user):
        #use set beacuse i want to prevent duplicate like
      if user.conected:
        if user not in self.how_like:
             self.how_like.add(user)
             self.User.notifications.append(f"{user._username} liked your post")
             print(f"notification to {self.User.get_username()}: {user._username} liked your post")
      else:
          raise (Exception("yore dont connected please connect first "))



    def unlike(self,user):
        #use set beacuse i want to prevent duplicate like
         self.how_like.remove(user)

    def comment(self,user,comment):
        if user.conected:
                if user.get_username() != self.User.get_username():
                     self.comments.append(user)
                     self.User.notifications.append(f"{user.get_username()} commented on your post")
                     print(f"notification to {self.User.get_username()}: {user.get_username()} commented on your post: {comment}")
        else:
            raise (Exception("yore dont connected please connect first "))

    @abstractmethod
    def __str__(self):
        pass

