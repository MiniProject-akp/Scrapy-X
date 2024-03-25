import customtkinter as ctk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageTk

# Function to scrape the website
def scrape_website():
    url = url_entry.get()
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('title').text
            output_text.set(title)  # Update the output_entry text
        else:
            messagebox.showerror("Error", f"Failed to retrieve the webpage. Status code: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to toggle light and dark mode
def toggle_mode():
    current_mode = ctk.get_appearance_mode()
    new_mode = "Light" if current_mode == "Dark" else "Dark"
    ctk.set_appearance_mode(new_mode)
    
    # Update background image for new mode
    image_path = "assets/lll.jpeg" if new_mode == "Light" else "path/to/your/dark_image.png"
    update_background_image(image_path)

# Update the background image
def update_background_image(image_path):
    new_background_image = Image.open(image_path)
    new_background_photo = ImageTk.PhotoImage(new_background_image)
    background_label.configure(image=new_background_photo)
    background_label.image = new_background_photo  # Keep a reference

ctk.set_appearance_mode("Dark")  # 'Light' or 'Dark'
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Web Scraper with Sidebar")
root.geometry("800x500")

# Background Image Setup
background_image = Image.open("assets/111.jpeg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = ctk.CTkLabel(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Sidebar for modes, messages, etc.
sidebar_frame = ctk.CTkFrame(root, width=200, corner_radius=0)
sidebar_frame.place(relx=0, rely=0, relheight=1)

# Main content area
main_frame = ctk.CTkFrame(root)
main_frame.place(relx=0.25, rely=0.1, relwidth=0.7, relheight=0.8)

# Sidebar Image Buttons
mode_button = ctk.CTkButton(sidebar_frame, text="Mode", command=toggle_mode, corner_radius=0)
mode_button.pack(fill="x", padx=10, pady=10)

message_button = ctk.CTkButton(sidebar_frame, text="Message", corner_radius=0)
message_button.pack(fill="x", padx=10, pady=10)

# URL Entry
url_entry = ctk.CTkEntry(main_frame, placeholder_text="Enter URL here", corner_radius=10)
url_entry.pack(pady=20)

output_text = ctk.StringVar()
output_entry = ctk.CTkEntry(main_frame, textvariable=output_text, placeholder_text="Output will appear here", corner_radius=10)
output_entry.pack(pady=10)

scrape_button = ctk.CTkButton(main_frame, text="Scrape", command=scrape_website, corner_radius=10)
scrape_button.pack(pady=10)

root.mainloop()