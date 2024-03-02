# Importing tkinter and PIL modules
import tkinter as tk
from PIL import Image, ImageTk

# Function to open the about window
def open_about():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_label = tk.Label(about_window, text="This is the homepage of your application.")
    about_label.pack()

# Function to open the user dashboard window
def open_user_dashboard():
    dashboard_window = tk.Toplevel(root)
    dashboard_window.title("User Dashboard")
    dashboard_label = tk.Label(dashboard_window, text="Welcome to your Dashboard!")
    dashboard_label.pack()

# Function to open the features window
def open_features():
    features_window = tk.Toplevel(root)
    features_window.title("Features")
    features_label = tk.Label(features_window, text="These are the features of our application.")
    features_label.pack()

# Function to open the signup window
def open_signup():
    signup_window = tk.Toplevel(root)
    signup_window.title("Signup")
    signup_label = tk.Label(signup_window, text="Signup page goes here.")
    signup_label.pack()

# Function to open the login window
def open_login():
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_label = tk.Label(login_window, text="Login page goes here.")
    login_label.pack()

# Creating the main Tkinter window
root = tk.Tk()
root.title("Homepage") # Title of the window
root.configure(bg='black')  # Background color of the window

# Creating a top frame for the navigation bar
top_frame = tk.Frame(root, bg="#240a88")  # Dark indigo color
top_frame.pack(fill="x")

# Load logo image and resize it
logo_image = Image.open(r"assets\logo.png")  # Replace with your own image path
logo_image = logo_image.resize((50, 50))
logo_photo = ImageTk.PhotoImage(logo_image)

# Add logo image
logo_label = tk.Label(top_frame, image=logo_photo, bg="#240a88")
logo_label.image = logo_photo  # Keep a reference to avoid garbage collection
logo_label.pack(side="left", padx=10)

# Add text logo
text_logo_label = tk.Label(top_frame, text="Scrapy-X", font=("Showcard Gothic", 16, "bold"), bg="#240a88", fg="white")
text_logo_label.pack(side="left")

# Add buttons to the top frame
features_button = tk.Button(top_frame, text="Features", command=open_features, bg="#240a88", fg="#D8BFD8")  # Light purple color
features_button.pack(side="left", padx=10)

about_button = tk.Button(top_frame, text="About Us", command=open_about, bg="#240a88", fg="#D8BFD8")  # Light purple color
about_button.pack(side="left", padx=10)

dashboard_button = tk.Button(top_frame, text="User Dashboard", command=open_user_dashboard, bg="#240a88", fg="#D8BFD8")  # Light purple color
dashboard_button.pack(side="left", padx=10)

signup_button = tk.Button(top_frame, text="Signup", command=open_signup, bg="#240a88", fg="#D8BFD8", width=10, height=2)  # Light purple color
signup_button.pack(side="right", padx=10)

login_button = tk.Button(top_frame, text="Login", command=open_login, bg="#240a88", fg="#D8BFD8", width=10, height=2)  # Light purple color
login_button.pack(side="right", padx=10)

# Load the picture to be displayed on the right side
picture_image = Image.open(r"assets\iii.png")  # Replace with your own image path
picture_image = picture_image.resize((800, 450))  # Resize the image as needed
picture_photo = ImageTk.PhotoImage(picture_image)

# Add picture to the right side
picture_label = tk.Label(root, image=picture_photo, bg='black')
picture_label.pack(side="right", fill="both", expand=True, padx=10, pady=10)  # Adjust padx and pady as needed

# Add text to the picture
text = "Welcome to our\n Application,\nWe hope you enjoy\n your experience!\n\n\nHarness it to boost your \nproductivty and creativity."
text_label = tk.Label(root, text=text, font=("Comic Sans MS", 24), bg='black', fg='white', justify='left')
text_label.pack(side="right", padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
