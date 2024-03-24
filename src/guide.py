import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("assets/side-img.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.pack(expand=True, side="left")

        frame = tk.Frame(self, width=300, height=480, bg="#ffffff")
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        tk.Label(frame, text="Welcome Back!", fg="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
        tk.Label(frame, text="Sign in to your account", fg="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

        tk.Label(frame, text="  Email:", fg="#601E88", anchor="w", justify="left", font=("Arial Bold", 14)).pack(anchor="w", pady=(38, 0), padx=(25, 0))
        tk.Entry(frame, width=30, fg="#000000").pack(anchor="w", padx=(25, 0))

        tk.Label(frame, text="  Password:", fg="#601E88", anchor="w", justify="left", font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0), padx=(25, 0))
        tk.Entry(frame, width=30, fg="#000000", show="*").pack(anchor="w", padx=(25, 0))

        tk.Button(frame, text="Login", fg="#601E88", font=("Arial Bold", 12), bg="#ffffff", activebackground="#ffffff", width=30).pack(anchor="w", pady=(40, 0), padx=(25, 0))
        tk.Button(frame, text="Continue With Google", fg="#601E88", font=("Arial Bold", 9), bg="#ffffff", activebackground="#ffffff", width=30).pack(anchor="w", pady=(20, 0), padx=(25, 0))

class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("assets/side-img.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.pack(expand=True, side="left")

        frame = tk.Frame(self, width=300, height=480, bg="#ffffff")
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        tk.Label(frame, text="Welcome To Scrapy-X", fg="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(20, 5), padx=(25, 0))
        tk.Label(frame, text="Please Fill Your Credentials", fg="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

        tk.Label(frame, text="  UserName:", fg="#601E88", anchor="w", justify="left", font=("Arial Bold", 14)).pack(anchor="w", pady=(10, 0), padx=(25, 0))
        tk.Entry(frame, width=30, fg="#000000").pack(anchor="w", padx=(25, 0))

        tk.Label(frame, text="  Purpose:", fg="#601E88", anchor="w", justify="left", font=("Arial Bold", 14)).pack(anchor="w", pady=(10, 0), padx=(25, 0))
        tk.Entry(frame, width=30, fg="#000000").pack(anchor="w", padx=(25, 0))

        tk.Label(frame, text="  Email:", fg="#601E88", anchor="w", justify="left", font=("Arial Bold", 14)).pack(anchor="w", pady=(10, 0), padx=(25, 0))
        tk.Entry(frame, width=30, fg="#000000").pack(anchor="w", padx=(25, 0))

        tk.Label(frame, text="  Password:", fg="#601E88", anchor="w", justify="left", font=("Arial Bold", 14)).pack(anchor="w", pady=(10, 0), padx=(25, 0))
        tk.Entry(frame, width=30, fg="#000000", show="*").pack(anchor="w", padx=(25, 0))

        tk.Button(frame, text="Sign Up", fg="#601E88", font=("Arial Bold", 12), bg="#ffffff", activebackground="#ffffff", width=30).pack(anchor="w", pady=(20, 0), padx=(25, 0))
        tk.Button(frame, text="Continue With Google", fg="#601E88", font=("Arial Bold", 9), bg="#ffffff", activebackground="#ffffff", width=30).pack(anchor="w", pady=(10, 0), padx=(25, 0))

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
 
        window = tk.Frame(self)
        window.pack()
 
        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)
 
        self.frames = {}
        for F in (LoginPage, RegisterPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
 
        self.show_frame(LoginPage)
 
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")

app = Application()
app.maxsize(800, 500)
app.mainloop()
