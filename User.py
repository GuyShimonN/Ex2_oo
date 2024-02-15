from FactoryPost import FactoryPost
from TextPost import TextPost


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.follwers = set()  # who see you
        self.Ifollowing = set()  # who you see
        self.notifications = []
        self.conected = True

    def add_follower(self, user):#add to the list that follwers(who see me)
        self.follwers.add(user)
    def unfollower(self,user):#remove from the list the follwers(who see me)
        self.follwers.remove(user)

    def get_username(self):
        return self.username

    # def publish_post(self, postType, *args):
    #     # send notification for all your followers
    #     FactoryPost(self, self.username, postType, *args)
    def publish_post(self, postType, *args):
        # send notification for all your followers
        # factory = FactoryPost()
        a = self
        post = FactoryPost.create_post(a, postType, *args)
        return post
    def print_notifications(self):
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
        user.add_follower(self.username)
        print(f"{self.username} started following {user.get_username()}")
    def unfollow(self, user):
        self.Ifollowing.remove(user.get_username())
        user.unfollower(self.username)
        print(f"{self.username} unfollowed {user.get_username()}")
