from tkinter import Tk, Entry, Button, Frame

# Define colors
bg_color = "#222831"
content_bg = "#2F353A"
text_color = "white"
border_color = "white"
placeholder_color = "#AAAAAA"
button_bg = "#363C43"
button_hover_bg = "#40464B"

# Create the main window
root = Tk()
root.title("Web Scraper")
root.configure(bg=bg_color)

# Create the content area
content_frame = Frame(root, bg=content_bg, bd=0, highlightthickness=0)
content_frame.pack(padx=20, pady=20)

# Style definition (optional - for future enhancements)
def button_enter(event):
    event.widget.config(bg=button_hover_bg)

def button_leave(event):
    event.widget.config(bg=button_bg)

# Text fields
url_entry = Entry(
    content_frame, width=50, bg=content_bg, fg=text_color, bd=1,  # Set border width
    # Removed unnecessary options related to highlight
    font=("Montserrat", 12), insertwidth=2,
    relief="flat",  # Set border style
    disabledforeground=placeholder_color
)
url_entry.insert(0, "Enter URL here")
url_entry.pack(pady=10)

output_entry = Entry(
    content_frame, width=50, bg=content_bg, fg=text_color, bd=1,  # Set border width
    # Removed unnecessary options related to highlight
    font=("Montserrat", 12), insertwidth=2,
    relief="flat",  # Set border style
    disabledforeground=placeholder_color
)
output_entry.insert(0, "Output will appear here")
output_entry.pack(pady=10)

# Button
scrape_button = Button(
    content_frame, text="Scrape", bg=button_bg, fg=text_color, bd=2, highlightthickness=0,
    font=("Montserrat", 12, "bold"), activebackground=button_hover_bg,
    activeforeground=text_color, relief="flat"
)
# Add hover animation (optional)
# scrape_button.bind("<Enter>", button_enter)
# scrape_button.bind("<Leave>", button_leave)
scrape_button.pack(pady=10)

# Run the main loop
root.mainloop()
