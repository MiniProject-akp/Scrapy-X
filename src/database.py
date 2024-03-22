import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql

def connect_to_database():
    try:
        # Connect to MySQL database
        connection = mysql.connect(host='localhost', user='root', password='Root', database='scrapyx')
        cursor = connection.cursor()
        messagebox.showinfo("Success", "Connected to MySQL database successfully!")
        # Close the cursor and connection
        cursor.close()
        connection.close()
    except mysql.Error as error:
        messagebox.showerror("Error", f"Failed to connect to MySQL database: {error}")

# Create the main Tkinter window
root = tk.Tk()
root.title("MySQL Database Connection")

# Create a button to connect to the database
connect_button = tk.Button(root, text="Connect to Database", command=connect_to_database)
connect_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
