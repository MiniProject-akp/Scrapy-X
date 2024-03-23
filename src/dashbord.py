import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def display_statistics():
    # Dummy function to display statistics
    print("Displaying statistics...")

def open_settings():
    # Dummy function to open settings
    print("Opening settings...")

def open_logs():
    # Dummy function to open logs
    print("Opening logs...")

# Create the main application window
root = tk.Tk()
root.title("Dashboard")

# Load the background image
background_image = Image.open("assets/sponge.png")
background_photo = ImageTk.PhotoImage(background_image)

# Set up the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Dashboard Title
title_label = ttk.Label(root, text="Dashboard", font=("Helvetica", 20, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# Statistics Section
statistics_frame = ttk.Frame(root)
statistics_frame.grid(row=1, column=0, padx=50, pady=50)
statistics_label = ttk.Label(statistics_frame, text="Statistics", font=("Helvetica", 16, "bold"))
statistics_label.pack()
statistics_button = ttk.Button(statistics_frame, text="Display Statistics", command=display_statistics)
statistics_button.pack(pady=5)

# Settings Section
settings_frame = ttk.Frame(root)
settings_frame.grid(row=2, column=0, padx=50, pady=50)
settings_label = ttk.Label(settings_frame, text="Settings", font=("Helvetica", 16, "bold"))
settings_label.pack()
settings_button = ttk.Button(settings_frame, text="Open Settings", command=open_settings)
settings_button.pack(pady=5)

# Logs Section
logs_frame = ttk.Frame(root)
logs_frame.grid(row=3, column=0, padx=50, pady=50)
logs_label = ttk.Label(logs_frame, text="Logs", font=("Helvetica", 16, "bold"))
logs_label.pack()
logs_button = ttk.Button(logs_frame, text="Open Logs", command=open_logs)
logs_button.pack(pady=5)

root.mainloop()
