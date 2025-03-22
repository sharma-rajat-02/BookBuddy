# Function to be called when the button is clicked
import tkinter as tk
from tkinter import messagebox
def on_button_click():
    messagebox.showinfo("Message Window","Button was clicked!")
    print("Button was clicked!")

# Create the main window
root = tk.Tk()
root.title("Button Example")

# Create a button widget
button = tk.Button(root, text="Click Me", command=on_button_click)

# Place the button in the window
button.pack(padx=20, pady=20)

# Start the Tkinter event loop
root.mainloop()