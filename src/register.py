import tkinter.messagebox
import subprocess
from customtkinter import *
from PIL import Image

def sign_in():
    # Retrieve values from entry fields
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Check if password and confirm password match
    if password == confirm_password:
        # Store credentials in a text file
        with open("credentials.txt", "w") as file:
            file.write(f"Username: {username}\nPassword: {password}")
        
        # Show sign-in success message
        tkinter.messagebox.showinfo("Success", "Sign in successful!")
        
        # Open scrapeyard.py file
        subprocess.Popen(["python", "C:/Users/depak/Scrapy-X/src/Srapeyard.py"])
        
        print("Credentials saved successfully!")
    else:
        print("Passwords do not match!")

app = CTk()
app.geometry("600x480")
app.resizable(0, 0)

side_img_data = Image.open("assets\\side-img.png")
user_icon_data = Image.open(r"assets\user.png")  # Use raw string with 'r' before the string
password_icon_data = Image.open("assets\\password-icon.png")

side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
user_icon = CTkImage(dark_image=user_icon_data, light_image=user_icon_data, size=(20, 20))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))

CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

CTkLabel(master=frame, text="Welcome To Scrapy-X", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(20, 5), padx=(25, 0))
CTkLabel(master=frame, text="Please Fill Your Credentials", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Username:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=user_icon, compound="left").pack(anchor="w", pady=(10, 0), padx=(25, 0))
username_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
username_entry.pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(10, 0), padx=(25, 0))
password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
password_entry.pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Confirm Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(10, 0), padx=(25, 0))
confirm_password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
confirm_password_entry.pack(anchor="w", padx=(25, 0))

CTkButton(master=frame, text="Sign in", command=sign_in, fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225).pack(anchor="w", pady=(20, 0), padx=(25, 0))

app.mainloop()
