import tkinter as tk

def navigate(page_name):
    content_label.config(text=f"Welcome to the {page_name} Page!")

root = tk.Tk()
root.title("Centered Navbar Dashboard")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

# 1. Main Navbar Background Stripe (Spans full width)
navbar = tk.Frame(root, bg="#2c3e50", height=50)
navbar.pack(side="top", fill="x")
navbar.pack_propagate(False) 

# 2. Centralized Button Container (Crucial part for centering)
# expand=True forces this sub-frame to center itself inside the main navbar
nav_container = tk.Frame(navbar, bg="#2c3e50")
nav_container.pack(expand=True, fill="y")

btn_styles = {
    "bg": "#2c3e50",
    "fg": "white",
    "activebackground": "#34495e",
    "activeforeground": "white",
    "bd": 0,
    "padx": 20, # Extra horizontal padding between items
    "font": ("Arial", 11, "bold"),
    "cursor": "hand2"
}

# 3. Pack buttons horizontally inside the centered container
home_btn = tk.Button(nav_container, text="Home", command=lambda: navigate("Home"), **btn_styles)
home_btn.pack(side="left", fill="y")

profile_btn = tk.Button(nav_container, text="Profile", command=lambda: navigate("Profile"), **btn_styles)
profile_btn.pack(side="left", fill="y")

settings_btn = tk.Button(nav_container, text="Settings", command=lambda: navigate("Settings"), **btn_styles)
settings_btn.pack(side="left", fill="y")

# Content Area
content_label = tk.Label(root, text="Select a page from the navbar", font=("Arial", 14), bg="#f0f0f0")
content_label.pack(expand=True)

root.mainloop()