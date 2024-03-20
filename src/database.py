from tkinter import*
from PIL import Image
import sqlite3

root=Tk()
root.title()
root.icombitmap()
root.geometry("400x400")

conn=sqlite3.connect('login.db','register.db')

c=conn.cursor()

c.execute()





conn.commit()



conn.close()