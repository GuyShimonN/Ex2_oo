from abc import ABC, abstractmethod

class Observer(ABC):
    def __init__(self):
        self.follwers = set()  # who see you

    def add_follower(self, User):#add to the list that follwers(who see me)
        self.follwers.add(User)
    def unfollower(self,user):#remove from the list the follwers(who see me)
        self.follwers.remove(user)
    def notify(self, meesege):
        for member in self.follwers:
            member.update(meesege)

