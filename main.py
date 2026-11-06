import tkinter as tk

def navigate(pageName):
    contentLabel.config(text = f"Welcome to the {pageName} page!")

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

homeBtn = tk.Button(navbar, text = "Home", command=lambda: navigate("Home"), **btnStyles)
homeBtn.pack(side = "left", fill = "y")

profileBtn = tk.Button(navbar, text = "Profile", command=lambda: navigate("Profile"), **btnStyles)
profileBtn.pack(side = "left", fill = "y")

settingsBtn = tk.Button(navbar, text = "Settings", command=lambda: navigate("Settings"), **btnStyles)
settingsBtn.pack(side = "left", fill = "y")

logoutBtn = tk.Button(navbar, text = "Logout", command=lambda: navigate("Logout"), **btnStyles)
logoutBtn.pack(side = "left", fill = "y")

contentLabel = tk.Button(root, text = "Select a page from the navbar", font = ("Arial", 14), bg = "#f0f0f0")
contentLabel.pack(expand = True)

# Main loop 

root.mainloop()