import tkinter as tk

def navigate(pageName):
    contentLabel.config(text = f"You selected: {pageName}")

# Window parameters

root = tk.Tk()
root.title("Navbar")
root.geometry("600x600")
root.configure(bg = "#f0f0f0")

# Navbar parameters

navbar = tk.Frame(root, bg = "#2c3e50", height = 50)
navbar.pack(side = "top", fill = "x")
navbar.pack_propagate(False)

# Button Styling

btnStyles = {
    "bg": "#2c3e50",
    "fg": "white",
    "activebackground": "#34495e",
    "activeforeground": "white",
    "bd": "0",
    "padx": "15",
    "font": ("Arial", 11, "bold"),
    "cursor": "hand2"
}

# Button configurations.

homeBtn = tk.Button(navbar, text = "Rock", command=lambda: navigate("Rock"), **btnStyles)
homeBtn.pack(side = "left", fill = "y")

profileBtn = tk.Button(navbar, text = "Paper", command=lambda: navigate("Paper"), **btnStyles)
profileBtn.pack(side = "left", fill = "y")

settingsBtn = tk.Button(navbar, text = "Scissors", command=lambda: navigate("Scissors"), **btnStyles)
settingsBtn.pack(side = "left", fill = "y")

contentLabel = tk.Button(root, text = "Please make a choice", font = ("Arial", 14), bg = "#f0f0f0")
contentLabel.pack(expand = True)

# Main loop 

root.mainloop()