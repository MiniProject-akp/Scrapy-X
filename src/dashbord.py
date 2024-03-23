import tkinter as tk
from tkinter import ttk

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

# Create a container to hold dashboard widgets
dashboard_container = ttk.Frame(root)
dashboard_container.pack(padx=20, pady=20)

# Dashboard Title
title_label = ttk.Label(dashboard_container, text="Dashboard", font=("Helvetica", 20, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Statistics Section
statistics_frame = ttk.Frame(dashboard_container, borderwidth=2, relief="solid", padding=(10, 10))
statistics_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
statistics_label = ttk.Label(statistics_frame, text="Statistics", font=("Helvetica", 16, "bold"))
statistics_label.pack()
statistics_button = ttk.Button(statistics_frame, text="Display Statistics", command=display_statistics)
statistics_button.pack(pady=5)

# Settings Section
settings_frame = ttk.Frame(dashboard_container, borderwidth=2, relief="solid", padding=(10, 10))
settings_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
settings_label = ttk.Label(settings_frame, text="Settings", font=("Helvetica", 16, "bold"))
settings_label.pack()
settings_button = ttk.Button(settings_frame, text="Open Settings", command=open_settings)
settings_button.pack(pady=5)

# Logs Section
logs_frame = ttk.Frame(dashboard_container, borderwidth=2, relief="solid", padding=(10, 10))
logs_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
logs_label = ttk.Label(logs_frame, text="Logs", font=("Helvetica", 16, "bold"))
logs_label.pack()
logs_button = ttk.Button(logs_frame, text="Open Logs", command=open_logs)
logs_button.pack(pady=5)

root.mainloop()
