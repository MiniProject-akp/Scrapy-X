import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from customtkinter import *

class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        side_img_data = Image.open("assets\side-img.png")
        email_icon_data = Image.open("assets\email-icon.png")
        password_icon_data = Image.open("assets\password-icon.png")

        side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
        email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
        password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))

        CTkLabel(master=self, text="", image=side_img).pack(expand=True, side="left")

        frame = CTkFrame(master=self, width=300, height=480, fg_color="#ffffff")
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
        CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

        CTkLabel(master=frame, text="  Username:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000").pack(anchor="w", padx=(25, 0))

        CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
        CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*").pack(anchor="w", padx=(25, 0))
    
        CTkButton(master=frame, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 0))
        CTkButton(master=frame, text="Register", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225).pack(anchor="w", pady=(20, 0), padx=(25, 0))

        def verify():
            try:
                with open("credential.txt", "r") as f:
                    info = f.readlines()
                    i = 0
                    for e in info:
                        u, p = e.split(",")
                        if u.strip() == Txt1.get() and p.strip() == TXT2.get():
                            controller.show_frame(SecondPage)
                            i = 1
                            break
                    if i == 0:
                        messagebox.showinfo(
                            "Error", "Please provide correct username and password!!")
            except:
                messagebox.showinfo(
                    "Error", "Please provide correct username and password!!")

        BTN1 = tk.Button(frame, text="Login",
                         font=("Arial", 15), command=verify)
        BTN1.place(x=370, y=300)

        def register():
            window = tk.Toplevel(self)
            window.geometry("470x220")
            window.resizable(0, 0)
            window.configure(bg="deep sky blue")
            window.title("Register")
            Label1 = tk.Label(window, text="Username:", font=(
                "Arial", 15), bg="deep sky blue")
            Label1.place(x=10, y=10)
            txt1 = tk.Entry(window, width=30, bd=5)
            txt1.place(x=200, y=10)

            lbl2 = tk.Label(window, text="Password:", font=(
                "Arial", 15), bg="deep sky blue")
            lbl2.place(x=10, y=60)
            txt2 = tk.Entry(window, width=30, show="*", bd=5)
            txt2.place(x=200, y=60)

            lbl3 = tk.Label(window, text="Confirm Password:",
                            font=("Arial", 15), bg="deep sky blue")
            lbl3.place(x=10, y=110)
            txt3 = tk.Entry(window, width=30, show="*", bd=5)
            txt3.place(x=200, y=110)

            def check():
                if txt1.get() != "" or txt2.get() != "" or txt3.get() != "":
                    if txt2.get() == txt3.get():
                        with open("credential.txt", "a") as f:
                            f.write(txt1.get()+","+txt2.get()+"\n")
                            messagebox.showinfo(
                                "Welcome", "You are registered successfully!!")
                    else:
                        messagebox.showinfo(
                            "Error", "Your password didn't get match!!")
                else:
                    messagebox.showinfo(
                        "Error", "Please fill the complete field!!")

            btn1 = tk.Button(window, text="Sign in", font=(
                "Arial", 15), bg="#ffc22a", command=check)
            btn1.place(x=170, y=150)

        BTN2 = tk.Button(self, text="Register", bg="dark orange",
                         font=("Arial", 15), command=register)
        BTN2.place(x=340, y=300)



class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("assets\\side-img.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        Button = tk.Button(self, text="Next", font=(
            "Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=650, y=450)

        Button = tk.Button(self, text="Back", font=(
            "Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=100, y=450)


class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg='Tomato')

        Label = tk.Label(self, text="Store some content related to your \n project or what your application made for. \n All the best!!",
                         bg="orange", font=("Arial Bold", 25))
        Label.place(x=40, y=150)

        Button = tk.Button(self, text="Home", font=(
            "Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=650, y=450)

        Button = tk.Button(self, text="Back", font=(
            "Arial", 15), command=lambda: controller.show_frame(SecondPage))
        Button.place(x=100, y=450)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")


app = Application()
app.maxsize(800, 500)
app.mainloop()

