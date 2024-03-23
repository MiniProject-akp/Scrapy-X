import tkinter as tk
from PIL import Image, ImageTk

class ImageWithEntryFieldApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image with Entry Field")
        self.root.geometry("600x400")

        # Load the image
        self.image = Image.open("assets\helpdesk.jpeg")  # Replace with your image path
        self.photo = ImageTk.PhotoImage(self.image)

        # Create a canvas to display the image
        self.canvas = tk.Canvas(root, width=self.image.width, height=self.image.height)
        self.canvas.pack()

        # Add the image to the canvas
        self.canvas.create_image(0, -50, anchor=tk.NW, image=self.photo)  # Adjust the y-coordinate to move the image upward

        # Get the dimensions of the image
        image_width, image_height = self.image.size

        # Create an entry field with a smaller size
        self.entry = tk.Entry(root, width=20)  # Adjust width as needed
        self.entry.place(x=50, y=image_height - 20, width=150, height=100)  # Adjust position and size of the entry field

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageWithEntryFieldApp(root)
    root.mainloop()
