import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def start_scrapy():
    print("Scrapy-X started!")

root = tk.Tk()
root.title("Homepage")

container = ttk.Frame(root, padding="20")
container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

title_label = ttk.Label(container, text="Welcome to SCRAPY-X!", font=("Arial", 20))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

description_label = ttk.Label(container, text="The FRIEND you need the most in today's era.", font=("Arial", 14))
description_label.grid(row=1, column=0, columnspan=2, pady=10)

# Load and display the image from the assets folder
image_path = "assets/what-is-social-media-scraping.png"
image = Image.open(image_path)
image = image.resize((300, 200), Image.ANTIALIAS)  # Resize the image to fit the window
photo = ImageTk.PhotoImage(image)
image_label = ttk.Label(container, image=photo)
image_label.grid(row=2, column=0, columnspan=2, pady=10)

start_button = ttk.Button(container, text="Let's start", command=start_scrapy)
start_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
