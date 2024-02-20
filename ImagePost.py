from post import post
import matplotlib.pyplot as plt

class ImagePost(post):
    def __init__(self,user,*args):
        super().__init__(user)
        temp ,=args[0] # unpack the the args
        self.image =temp  # unpack the the args
        print(f"{self.User.username} posted a picture\n")

    def __str__(self):
        return f"{self.User.username} posted a picture\n"

    def display(self):
        print("Shows picture")
        image_rgb = plt.imread(self.image)
        plt.imshow(image_rgb)
        plt.axis('off')
        plt.show()
