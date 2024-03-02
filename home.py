import tkinter as tk
from PIL import Image, ImageTk
import subprocess

class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Homepage")
        self.root.configure(bg='black')

    
        picture_image = Image.open("assets/pic.jpeg")  
        picture_image = picture_image.resize((800, 450)) 
        self.picture_photo = ImageTk.PhotoImage(picture_image)

        # Create a canvas for the image
        self.canvas = tk.Canvas(root, width=800, height=450, bg='black')
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.picture_photo)
        self.canvas.pack(side="right", padx=10, pady=10)

       
        heading_label = tk.Label(root, text="                                    Welcome to Scrapy-X", font=("Arial", 20, "bold"), fg="black", bg='yellow')
        heading_label_window = self.canvas.create_window(10, 10, anchor=tk.NW, window=heading_label)

        login_button = tk.Button(root, text="Login", bg="black", fg="white", font=("Bebas", 16, "bold"),
                                 relief=tk.RIDGE, bd=2, command=self.open_login)
        login_button_window = self.canvas.create_window(370, 150, anchor=tk.NW, window=login_button)

        signup_button = tk.Button(root, text="Signup", bg="black", fg="white", font=("Bebas", 16, "bold"),
                                  relief=tk.RIDGE, bd=2, command=self.open_signup)
        signup_button_window = self.canvas.create_window(370, 200, anchor=tk.NW, window=signup_button)

    def open_login(self):
        subprocess.run(["python", "login.py"])

    def open_signup(self):
        print("Signup button clicked")

if __name__ == "__main__":
    root = tk.Tk()
    app = HomePage(root)
    root.mainloop()
