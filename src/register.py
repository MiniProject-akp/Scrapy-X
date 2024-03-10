
import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue") 
appWidth, appHeight = 600, 700

class App(ctk.CTk):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
  
        self.title("Registration Page") 
        self.geometry(f"{appWidth}x{appHeight}") 

        self.createAccountLabel = ctk.CTkLabel(self,
                                text="Create Account",
                                font=("Arial", 16, "bold"),
                                pady=10)
        self.createAccountLabel.grid(row=0, column=0,
                            columnspan=4,
                            padx=20, pady=20,
                            sticky="ew")

        self.nameLabel = ctk.CTkLabel(self,
                                text="Name")
        self.nameLabel.grid(row=1, column=0,
                            padx=20, pady=10,
                            sticky="ew")

        self.nameEntry = ctk.CTkEntry(self,
                        placeholder_text="John Doe")
        self.nameEntry.grid(row=1, column=1,
                            columnspan=3, padx=20,
                            pady=10, sticky="ew")

        self.emailLabel = ctk.CTkLabel(self,
                                text="Email")
        self.emailLabel.grid(row=2, column=0,
                            padx=20, pady=10,
                            sticky="ew")

        self.emailEntry = ctk.CTkEntry(self,
                        placeholder_text="example@example.com")
        self.emailEntry.grid(row=2, column=1,
                            columnspan=3, padx=20,
                            pady=10, sticky="ew")

        self.createPasswordLabel = ctk.CTkLabel(self, text="Create Password")
        self.createPasswordLabel.grid(row=3, column=0,
                        padx=20, pady=10,
                        sticky="ew")

        self.createPasswordEntry = ctk.CTkEntry(self,
                            placeholder_text="Password", show="*")
        self.createPasswordEntry.grid(row=3, column=1,
                        columnspan=3, padx=20,
                        pady=10, sticky="ew")

        self.confirmPasswordLabel = ctk.CTkLabel(self, text="Confirm Password")
        self.confirmPasswordLabel.grid(row=4, column=0,
                        padx=20, pady=10,
                        sticky="ew")

        self.confirmPasswordEntry = ctk.CTkEntry(self,
                            placeholder_text="Confirm Password", show="*")
        self.confirmPasswordEntry.grid(row=4, column=1,
                        columnspan=3, padx=20,
                        pady=10, sticky="ew")

        self.occupationLabel = ctk.CTkLabel(self,
                                    text="Occupation")
        self.occupationLabel.grid(row=5, column=0,
                                padx=20, pady=10,
                                sticky="ew")

        self.occupationOptionMenu = ctk.CTkOptionMenu(self,
                                    values=["Student", "Professional"])
        self.occupationOptionMenu.grid(row=5, column=1,
                                    columnspan=3, padx=20,
                                    pady=10, sticky="ew")

        self.registerButton = ctk.CTkButton(self,
                                        text="Register",
                                        command=self.register)
        self.registerButton.grid(row=6, column=1,
                                        columnspan=2, padx=20, 
                                        pady=20, sticky="ew")

    def register(self):
        text = self.createText()
        print(text)
    
    def createText(self):
        text = f"Name: {self.nameEntry.get()} \nEmail: {self.emailEntry.get()} \nOccupation: {self.occupationOptionMenu.get()}"
        return text

if __name__ == "__main__":
    app = App()
    app.mainloop()	 
