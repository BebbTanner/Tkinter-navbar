import tkinter as tk

def navigate(pageName):
    content_label.config(text = f"Welcome to the {pageName} page!")

# Window parameters

root = tk.Tk()
root.title("Navbar")
root.geometry("600x600")
root.configure(bg = "#f0f0f0")

# Navbar parameters

navbar = tk.Frame(root, bg = "#2c3e50", height = 50)
navbar.pack(side = "top", fill = "x")
navbar.pack_propagate(False)

