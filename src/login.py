import tkinter.messagebox
import subprocess
from customtkinter import *
from PIL import Image

def login():
    # Retrieve values from entry fields
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # Read credentials from credentials.txt
    with open("credentials.txt", "r") as file:
        lines = file.readlines()
        saved_username = lines[0].strip().split(":")[1]
        saved_password = lines[1].strip().split(":")[1]

    print("Entered Username:", entered_username)
    print("Entered Password:", entered_password)
    print("Saved Username:", saved_username)
    print("Saved Password:", saved_password)

    # Check if entered credentials match with saved credentials
    if entered_username == saved_username and entered_password == saved_password:
        # Show login successful message
        tkinter.messagebox.showinfo("Success", "Login successful!")
        
        # Open scrapeyard.py file
        subprocess.Popen(["python", "C:/Users/depak/Scrapy-X/src/Srapeyard.py"])
    else:
        tkinter.messagebox.showerror("Error", "Invalid username or password")


app = CTk()
app.geometry("600x480")
app.resizable(0,0)

side_img_data = Image.open("assets\side-img.png")
email_icon_data = Image.open("assets\email-icon.png")
password_icon_data = Image.open("assets\password-icon.png")

side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))

CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Username:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
username_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
username_entry.pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
password_entry.pack(anchor="w", padx=(25, 0))

CTkButton(master=frame, text="Login", command=login, fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 0))
CTkButton(master=frame, text="Register", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225).pack(anchor="w", pady=(20, 0), padx=(25, 0))

app.mainloop()
