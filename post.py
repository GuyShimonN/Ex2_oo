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
           #if user.username == self.User.username:
             self.how_like.add(user)
             self.User.notifications.append(f"{user.username} liked your post")
             print(f"notification to {self.User.get_username()}: {user.username} liked your post")
      else:
          raise (Exception("yore dont connected please connect first "))



    def unlike(self,user):
        #use set beacuse i want to prevent duplicate like
         self.how_like.remove(user)

    def comment(self,user,comment):
        #use at dictonrt the key: user value:comment
        if user.conected:
            #if user.username != self.User.username:
                if user.username != self.User.username:
                     self.comments.append(user)
                     self.User.notifications.append(f"{user.username} commented on your post")
                     print(f"notification to {self.User.username}: {user.username} commented on your post: {comment}")
        else:
            raise (Exception("yore dont connected please connect first "))

    @abstractmethod
    def __str__(self):
        pass

