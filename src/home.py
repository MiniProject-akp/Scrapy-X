import tkinter as tk
from PIL import Image, ImageTk
import subprocess

class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Homepage")
        self.root.configure(bg='black')

    
        picture_image = Image.open("assets/Home.png")  
        picture_image = picture_image.resize((800, 450)) 
        self.picture_photo = ImageTk.PhotoImage(picture_image)

        # Create a canvas for the image
        self.canvas = tk.Canvas(root, width=800, height=450, bg='black')
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.picture_photo)
        self.canvas.pack(side="right", padx=10, pady=10)

       
        heading_label = tk.Label(root, text="                                    Welcome to Scrapy-X", font=("Showcard Gothic", 20, "bold"), fg="white", bg='indigo')
        heading_label_window = self.canvas.create_window(10, 10, anchor=tk.NW, window=heading_label)

        login_button = tk.Button(root, text="Login", bg="red", fg="white", font=("Times New Roman", 16, "bold"),
                                 relief=tk.RIDGE, bd=2, command=self.open_login)
        login_button_window = self.canvas.create_window(10, 350, anchor=tk.NW, window=login_button)

        signup_button = tk.Button(root, text="Signup", bg="green", fg="white", font=("Times New Roman", 16, "bold"),
                                  relief=tk.RIDGE, bd=2, command=self.open_signup)
        signup_button_window = self.canvas.create_window(10, 400, anchor=tk.NW, window=signup_button)
        
        helpdesk_button = tk.Button(root, text="Helpdesk", bg="indigo", fg="white", font=("Times New Roman", 16, "bold"),
                                  relief=tk.RIDGE, bd=2, command=self.open_helpdesk)
        helpdesk_button_window = self.canvas.create_window(100, 400, anchor=tk.NW, window=helpdesk_button)
        
        dashbord_button = tk.Button(root, text="Dashboard", bg="indigo", fg="white", font=("Times New Roman", 16, "bold"),
                                  relief=tk.RIDGE, bd=2, command=self.open_dashbord)
        dashbord_button_window = self.canvas.create_window(100, 350, anchor=tk.NW, window=dashbord_button)
        
        mainpage_button = tk.Button(root, text="Mainpage", bg="indigo", fg="white", font=("Times New Roman", 16, "bold"),
                                  relief=tk.RIDGE, bd=2, command=self.open_mainpage)
        mainpage_button_window = self.canvas.create_window(235, 350, anchor=tk.NW, window=mainpage_button)
        
        guide_button = tk.Button(root, text="Guide", bg="indigo", fg="white", font=("Times New Roman", 16, "bold"),
                                  relief=tk.RIDGE, bd=2, command=self.open_guide)
        guide_button_window = self.canvas.create_window(235, 400, anchor=tk.NW, window=guide_button)








    def open_login(self):
        subprocess.run(["python", "login.py"])

    def open_signup(self):
        subprocess.run(["python", "register.py"])
        
    def open_helpdesk(self):
        subprocess.run(["python", "helpdesk.py"])
        
    def open_dashbord(self):
        subprocess.run(["python", "dashbord.py"])
        
    def open_mainpage(self):
        subprocess.run(["python", "mainpage.py"])
        
    def open_guide(self):
        subprocess.run(["python", "guide.py"])




if __name__ == "__main__":
    root = tk.Tk()
    app = HomePage(root)
    root.mainloop()
