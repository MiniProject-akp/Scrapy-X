from customtkinter import *
from tkinter import messagebox
import pymysql

def connect_database():
    # Connect to the database
    try:
        con = pymysql.connect(host='localhost', user='root', password='Shrey@s124')
        mycursor = con.cursor()
    except pymysql.Error as e:
        messagebox.showerror('Error', f'Database Connectivity Issue: {e}')
        return

    # Create the database and table if they don't exist
    try:
        mycursor.execute('CREATE DATABASE IF NOT EXISTS userdata')
        mycursor.execute('USE userdata')
        mycursor.execute('CREATE TABLE IF NOT EXISTS data(id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50), username VARCHAR(50), password VARCHAR(20))')
    except pymysql.Error as e:
        messagebox.showerror('Error', f'Database Operation Issue: {e}')
        con.close()
        return

    # Check if username already exists
    try:
        query = 'SELECT * FROM data WHERE username=%s'
        mycursor.execute(query, (email_entry.get(),))
        row = mycursor.fetchone()
        if row is not None:
            messagebox.showerror('Error', 'Username Already Exists')
            con.close()
            return
    except pymysql.Error as e:
        messagebox.showerror('Error', f'Database Operation Issue: {e}')
        con.close()
        return

    # Insert data into the database
    try:
        query = 'INSERT INTO data(first_name, last_name, username, password) VALUES (%s, %s, %s, %s)'
        mycursor.execute(query, (first_name_entry.get(), last_name_entry.get(), email_entry.get(), password_entry.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Success', 'Sign Up Successful')
        clear_entries()
        # Redirect to login page
        app.destroy()
        import login  # Assuming login.py contains the login page code
        login.page()
    except pymysql.Error as e:
        messagebox.showerror('Error', f'Database Operation Issue: {e}')
        con.close()
        return

def clear_entries():
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)

app = CTk()
app.geometry("600x480")
app.resizable(0, 0)

# Creating Labels and Entries
first_name_entry = CTkEntry(master=app, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
last_name_entry = CTkEntry(master=app, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
email_entry = CTkEntry(master=app, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
password_entry = CTkEntry(master=app, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")

# Creating Buttons
signup_button = CTkButton(master=app, text="Sign Up", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=connect_database)

# Packing GUI elements
# Packing of Labels and Entries
first_name_entry.pack(anchor="w", padx=(25, 0))
last_name_entry.pack(anchor="w", padx=(25, 0))
email_entry.pack(anchor="w", padx=(25, 0))
password_entry.pack(anchor="w", padx=(25, 0))
# Packing of Buttons
signup_button.pack(anchor="w", pady=(20, 0), padx=(25, 0))

app.mainloop()
