from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Feedback:

    def __init__(self, master):

        master.title('SCRAPY-X  USER  REVIEW')
        master.resizable(False, False)
        master.configure(background='#000000')  

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#000000')
        self.style.configure('TButton', background='#000000', foreground='white', font=('Barlow', 11))  
        self.style.configure('TLabel', background='#000000', font=('Barlow', 11, 'bold'), foreground='white')
        self.style.configure('header.TLabel', font=('Barlow', 18, 'bold'), foreground='white')

        self.frame_header = ttk.Frame(master)  # header frame
        self.frame_header.pack()

        ttk.Label(self.frame_header, text="Thanks for Exploring!", style='header.TLabel').grid(row=0, column=0)
        ttk.Label(self.frame_header, text="We're glad you chose to explore SCRAPY-X!\nPlease tell us how it was.",
                  justify='center').grid(row=1, column=0)

        self.frame_content = ttk.Frame(master)  
        self.frame_content.pack(pady=10)  

        ttk.Label(self.frame_content, text='Name:').grid(row=0, column=0, padx=5, pady=5, sticky='sw')  
        ttk.Label(self.frame_content, text='Email:').grid(row=0, column=1, padx=5, pady=5, sticky='sw')  
        ttk.Label(self.frame_content, text='Comments:').grid(row=2, column=0, padx=5, pady=5, sticky='sw')  

        self.entry_name = ttk.Entry(self.frame_content, width=24, font=('Barlow', 10))
        self.entry_email = ttk.Entry(self.frame_content, width=24, font=('Barlow', 10))
        self.text_comments = Text(self.frame_content, width=50, height=5, font=('Barlow', 10), foreground='white')  

        self.entry_name.grid(row=1, column=0, padx=5, pady=5)  
        self.entry_email.grid(row=1, column=1, padx=5, pady=5)  
        self.text_comments.grid(row=3, column=0, columnspan=2, padx=5, pady=5)  

        ttk.Button(self.frame_content, text='Submit', command=self.submit, style='SubmitButton.TButton').grid(row=4, column=0, padx=5, pady=5, sticky='e')  
        ttk.Button(self.frame_content, text='Clear', command=self.clear, style='ClearButton.TButton').grid(row=4, column=1, padx=5, pady=5, sticky='w')  

        self.style.configure('SubmitButton.TButton', foreground='black', font=('Barlow', 11, 'bold'))
        self.style.configure('ClearButton.TButton', foreground='black', font=('Barlow', 11, 'bold'))

    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
        self.clear()
        messagebox.showinfo(title="SCRAPY-X User Review", message="Comments Submitted!")

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')


def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()


if __name__ == "__main__":
    main()
