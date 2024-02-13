from FactoryPost import FactoryPost
from TextPost import TextPost



class User:
    def __init__(self,username,password):
        self.username = username
        self.password =password
        self.follwers=[] #who see you
        self.following=[] #who you see
        self.notifications =[]

    def add_follower(self,user):
        self.follwers.append(user)

    def unfollow(self,user):
        self.following.remove(user)

    def add_following(self,user):
      self.following.append(user)

    def get_username(self):
        return self.username

    def publish_post(self, postType, *args):
        #send notification for all your followers
       FactoryPost(self,self.username,postType, *args)
    def print_notifications(self):
        for note in self.notifications:
            print(note)
    def get_Password(self):
        return self.password