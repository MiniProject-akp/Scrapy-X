# Python program to create a basic form 
# GUI application using the customtkinter module
import customtkinter as ctk
import tkinter as tk

# Sets the appearance of the window
# Supported modes : Light, Dark, System
# "System" sets the appearance mode to 
# the appearance mode of the system
ctk.set_appearance_mode("dark") 

# Sets the color of the widgets in the window
# Supported themes : green, dark-blue, blue 
ctk.set_default_color_theme("blue") 

# Dimensions of the window
appWidth, appHeight = 600, 700


# App Class
class App(ctk.CTk):
    # The layout of the window will be written
    # in the init function itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sets the title of the window to "App"
        self.title("Registration Page") 
        # Sets the dimensions of the window to 600x700
        self.geometry(f"{appWidth}x{appHeight}") 

        # Create Account Label
        self.createAccountLabel = ctk.CTkLabel(self,
                                text="Create Account",
                                font=("Arial", 16, "bold"),
                                pady=10)
        self.createAccountLabel.grid(row=0, column=0,
                            columnspan=4,
                            padx=20, pady=20,
                            sticky="ew")

        # Name Label
        self.nameLabel = ctk.CTkLabel(self,
                                text="Name")
        self.nameLabel.grid(row=1, column=0,
                            padx=20, pady=10,
                            sticky="ew")

        # Name Entry Field
        self.nameEntry = ctk.CTkEntry(self,
                        placeholder_text="John Doe")
        self.nameEntry.grid(row=1, column=1,
                            columnspan=3, padx=20,
                            pady=10, sticky="ew")

        # Email Label
        self.emailLabel = ctk.CTkLabel(self,
                                text="Email")
        self.emailLabel.grid(row=2, column=0,
                            padx=20, pady=10,
                            sticky="ew")

        # Email Entry Field
        self.emailEntry = ctk.CTkEntry(self,
                        placeholder_text="example@example.com")
        self.emailEntry.grid(row=2, column=1,
                            columnspan=3, padx=20,
                            pady=10, sticky="ew")

        # Create Password Label
        self.createPasswordLabel = ctk.CTkLabel(self, text="Create Password")
        self.createPasswordLabel.grid(row=3, column=0,
                        padx=20, pady=10,
                        sticky="ew")

        # Create Password Entry Field
        self.createPasswordEntry = ctk.CTkEntry(self,
                            placeholder_text="Password", show="*")
        self.createPasswordEntry.grid(row=3, column=1,
                        columnspan=3, padx=20,
                        pady=10, sticky="ew")

        # Confirm Password Label
        self.confirmPasswordLabel = ctk.CTkLabel(self, text="Confirm Password")
        self.confirmPasswordLabel.grid(row=4, column=0,
                        padx=20, pady=10,
                        sticky="ew")

        # Confirm Password Entry Field
        self.confirmPasswordEntry = ctk.CTkEntry(self,
                            placeholder_text="Confirm Password", show="*")
        self.confirmPasswordEntry.grid(row=4, column=1,
                        columnspan=3, padx=20,
                        pady=10, sticky="ew")

        # Occupation Label
        self.occupationLabel = ctk.CTkLabel(self,
                                    text="Occupation")
        self.occupationLabel.grid(row=5, column=0,
                                padx=20, pady=10,
                                sticky="ew")

        # Occupation combo box
        self.occupationOptionMenu = ctk.CTkOptionMenu(self,
                                    values=["Student", "Professional"])
        self.occupationOptionMenu.grid(row=5, column=1,
                                    columnspan=3, padx=20,
                                    pady=10, sticky="ew")

        # Register Button
        self.registerButton = ctk.CTkButton(self,
                                        text="Register",
                                        command=self.register)
        self.registerButton.grid(row=6, column=1,
                                        columnspan=2, padx=20, 
                                        pady=20, sticky="ew")

    # This function is used to insert the 
    # details entered by users into the textbox
    def register(self):
        text = self.createText()
        print(text)

    # This function is used to get the selected 
    # options and text from the available entry
    # fields and boxes and then generates 
    # a prompt using them
    def createText(self):
        text = f"Name: {self.nameEntry.get()} \nEmail: {self.emailEntry.get()} \nOccupation: {self.occupationOptionMenu.get()}"
        return text

if __name__ == "__main__":
    app = App()
    # Used to run the application
    app.mainloop()	 
