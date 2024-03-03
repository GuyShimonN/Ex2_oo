from post import post
import matplotlib.pyplot as plt  # Importing matplotlib for image display

class ImagePost(post):  # ImagePost class inheriting from post
    def __init__(self,user,*args):  # Constructor method
        super().__init__(user)  # Call the constructor of his father (post)
        temp ,=args[0]  # Unpack the args
        self.image =temp
        print(f"{self.User._username} posted a picture\n")

    def __str__(self):
        return f"{self.User._username} posted a picture\n"  # Return a string indicating picture posting

    def display(self):
        print("Shows picture")
        image_rgb = plt.imread(self.image)  # Read the image file
        plt.imshow(image_rgb)  # Display the image
        plt.axis('off')  # Turn off axis
        plt.show()  # Show the image
