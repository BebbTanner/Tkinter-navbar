import tkinter as tk

def navigate(pageName):
    content_label.config(text = f"Welcome to the {pageName} page!")

# Window parameters

root = tk.Tk()
root.title("Navbar")
root.geometry("600x600")
root.configure(bg = "#f0f0f0")
