from FactoryPost import FactoryPost
from Member import Member
from Observer import Observer
from TextPost import TextPost


class User(Observer,Member):
    def __init__(self, username, password):
        self.Number_of_posts=0
        Observer.__init__(self)
        self.username = username
        self.password = password
        # self.follwers = set()  # who see you
        self.Ifollowing = set()  # who you see
        self.notifications = []
        self.conected = True

    # def add_follower(self, user):#add to the list that follwers(who see me)
    #     self.follwers.add(user)
    # def unfollower(self,user):#remove from the list the follwers(who see me)
    #     self.follwers.remove(user)

    def get_username(self):
        return self.username

    # def publish_post(self, postType, *args):
    #     # send notification for all your followers
    #     FactoryPost(self, self.username, postType, *args)
    def publish_post(self, postType, *args):
        # send notification for all your followers
        # factory = FactoryPost()
       if self.conected:
            post = FactoryPost.create_post(self, postType, *args)
        # self.notifications.append(post)
            self.Number_of_posts +=1

            self.notify(f"{self.username} has a new post")
            return post
       else:
        raise (Exception("yore dont connected please connect first "))

    def print_notifications(self):
        print(f"{self.username}'s notifications:")
        for note in self.notifications:
            print(note)

    def get_Password(self):
        return self.password

    def get_concted(self):
        return self.conected

    def set_concted(self, bolian):
        self.conected = bolian

    def follow(self, user):
        self.Ifollowing.add(user.get_username())
        user.add_follower(self)
        print(f"{self.username} started following {user.get_username()}")
    def unfollow(self, user):
      if self.conected:
        self.Ifollowing.remove(user.get_username())
        user.unfollower(self)
        print(f"{self.username} unfollowed {user.get_username()}")
      else:
          raise (Exception("yore dont connected"))

    def update(self, meesege):
        self.notifications.append(meesege)
    def __str__(self):
        return f"User name: {self.username}, Number of posts: {self.Number_of_posts},Number of followers: {self.follwers.__len__()}"