# Importing tkinter and PIL modules
import tkinter as tk
from PIL import Image, ImageTk

# Function to open the about window
def open_about():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_label = tk.Label(about_window, text="This is the homepage of your application.")
    about_label.pack()

# Function to open the blog window
def open_blog():
    blog_window = tk.Toplevel(root)
    blog_window.title("Blog")
    blog_label = tk.Label(blog_window, text="Welcome to our Blog!")
    blog_label.pack()

# Function to open the user manual window
def open_user_manual():
    manual_window = tk.Toplevel(root)
    manual_window.title("User Manual")
    manual_label = tk.Label(manual_window, text="User Manual goes here.")
    manual_label.pack()

# Creating the main Tkinter window
root = tk.Tk()
root.title("Homepage") # Title of the window
root.configure(bg='black')  # Background color of the window

# Creating a top frame for the navigation bar
top_frame = tk.Frame(root, bg="#240a88")  # Dark indigo color
top_frame.pack(fill="x")

# Load logo image and resize it
logo_image = Image.open(r"assets\tt.png")  # Replace with your own image path
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
features_button = tk.Button(top_frame, text="Features", bg="#240a88", fg="#D8BFD8")  # Light purple color
features_button.pack(side="left", padx=10)

about_button = tk.Button(top_frame, text="About Us", command=open_about, bg="#240a88", fg="#D8BFD8")  # Light purple color
about_button.pack(side="left", padx=10)

blog_button = tk.Button(top_frame, text="Blog", command=open_blog, bg="#240a88", fg="#D8BFD8")  # Light purple color
blog_button.pack(side="left", padx=10)

manual_button = tk.Button(top_frame, text="User Manual", command=open_user_manual, bg="#240a88", fg="#D8BFD8")  # Light purple color
manual_button.pack(side="left", padx=10)

signup_button = tk.Button(top_frame, text="Signup", bg="#240a88", fg="#D8BFD8")  # Light purple color
signup_button.pack(side="right", padx=10)

login_button = tk.Button(top_frame, text="Login", bg="#240a88", fg="#D8BFD8")  # Light purple color
login_button.pack(side="right", padx=10)

# Load the picture to be displayed on the right side
picture_image = Image.open(r"assets\iii.png")  # Replace with your own image path
picture_image = picture_image.resize((800, 450))  # Resize the image as needed
picture_photo = ImageTk.PhotoImage(picture_image)

# Add picture to the right side
picture_label = tk.Label(root, image=picture_photo, bg='black')
picture_label.pack(side="right", padx=10, pady=10)  # Adjust padx and pady as needed

# Run the Tkinter event loop
root.mainloop()
