import tkinter as tk
from PIL import Image, ImageTk
import subprocess

class HomePage(tk.Frame):
    def __init__(self, master, show_login, show_signup, show_helpdesk, show_dashboard, show_mainpage, show_guide):
        super().__init__(master)
        self.master = master
        self.configure(bg='black')

        picture_image = Image.open("assets/Home.png")
        picture_image = picture_image.resize((800, 450))
        self.picture_photo = ImageTk.PhotoImage(picture_image)

        # Create a canvas for the image
        self.canvas = tk.Canvas(self, width=800, height=450, bg='black')
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.picture_photo)
        self.canvas.pack(side="right", padx=10, pady=10)

        heading_label = tk.Label(self, text="Welcome to Scrapy-X", font=("Showcard Gothic", 20, "bold"), fg="white", bg='indigo')
        heading_label_window = self.canvas.create_window(10, 10, anchor=tk.NW, window=heading_label)

        login_button = tk.Button(self, text="Login", bg="red", fg="white", font=("Times New Roman", 16, "bold"),
                                 relief=tk.RIDGE, bd=2, command=show_login)
        login_button_window = self.canvas.create_window(10, 350, anchor=tk.NW, window=login_button)

        signup_button = tk.Button(self, text="Signup", bg="green", fg="white", font=("Times New Roman", 16, "bold"),
                                  relief=tk.RIDGE, bd=2, command=show_signup)
        signup_button_window = self.canvas.create_window(10, 400, anchor=tk.NW, window=signup_button)

        helpdesk_button = tk.Button(self, text="Helpdesk", bg="indigo", fg="white", font=("Times New Roman", 16, "bold"),
                                    relief=tk.RIDGE, bd=2, command=show_helpdesk)
        helpdesk_button_window = self.canvas.create_window(100, 400, anchor=tk.NW, window=helpdesk_button)

        dashboard_button = tk.Button(self, text="Dashboard", bg="indigo", fg="white", font=("Times New Roman", 16, "bold"),
                                      relief=tk.RIDGE, bd=2, command=show_dashboard)
        dashboard_button_window = self.canvas.create_window(100, 350, anchor=tk.NW, window=dashboard_button)

        mainpage_button = tk.Button(self, text="Mainpage", bg="indigo", fg="white", font=("Times New Roman", 16, "bold"),
                                    relief=tk.RIDGE, bd=2, command=show_mainpage)
        mainpage_button_window = self.canvas.create_window(235, 350, anchor=tk.NW, window=mainpage_button)

        guide_button = tk.Button(self, text="Guide", bg="indigo", fg="white", font=("Times New Roman", 16, "bold"),
                                  relief=tk.RIDGE, bd=2, command=show_guide)
        guide_button_window = self.canvas.create_window(235, 400, anchor=tk.NW, window=guide_button)

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Homepage")
        self.geometry("800x450")
        self.configure(bg='black')

        self.home_page = HomePage(self, self.show_login, self.show_signup, self.show_helpdesk, self.show_dashboard,
                                  self.show_mainpage, self.show_guide)
        self.current_page = None
        self.show_page(self.home_page)

    def show_page(self, page):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = page
        self.current_page.pack(fill=tk.BOTH, expand=True)

    def show_login(self):
        # Open the specified file in the terminal
        subprocess.run(["python", "C:/Users/Jha/Scrapy-X/src/login.py"])

    def show_signup(self):
        subprocess.run(["python", "C:/Users/Jha/Scrapy-X/src/register.py"])

    def show_helpdesk(self):
        subprocess.run(["python", "C:/Users/Jha/Scrapy-X/src/helpdesk.py"])

    def show_dashboard(self):
        subprocess.run(["python", "C:/Users/Jha/Scrapy-X/src/dashbord.py"])


    def show_mainpage(self):
        subprocess.run(["python", "C:/Users/Jha/Scrapy-X/src/mainpage.py"])


    def show_guide(self):
        subprocess.run(["python", "C:/Users/Jha/Scrapy-X/src/guide.py"])


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
