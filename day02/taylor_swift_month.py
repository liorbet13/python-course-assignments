import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os

def get_taylor_swift_album(month_source=None):
    """Get the Taylor Swift album based on birth month"""
    # Dictionary mapping month names to Taylor Swift albums
    month_to_album = {
        "January": "Taylor Swift",
        "February": "Fearless",
        "March": "Speak Now",
        "April": "Red",
        "May": "1989",
        "June": "Reputation",
        "July": "Lover",
        "August": "Folklore",
        "September": "Evermore",
        "October": "Midnights",
        "November": "The Tortured Poets Department",
        "December": "The Life of a Showgirl"
    }
    
    # Dictionary mapping album names to image filenames
    album_to_image = {
        "Taylor Swift": "taylor_swift.jpg",
        "Fearless": "fearless.jpg",
        "Speak Now": "speak_now.jpg",
        "Red": "red.jpg",
        "1989": "1989.jpg",
        "Reputation": "reputation.jpg",
        "Lover": "lover.jpg",
        "Folklore": "folklore.jpg",
        "Evermore": "evermore.jpg",
        "Midnights": "midnights.jpg",
        "The Tortured Poets Department": "ttpd.jpg",
        "The Life of a Showgirl": "showgirl.jpg"
    }
    
    # Get month from the specified source or from text entry
    if month_source:
        month_name = month_source
    else:
        month_name = month_entry.get().strip().capitalize()  # Capitalize first letter
    
    if month_name in month_to_album:
        album_name = month_to_album[month_name]
        
        result_label.config(
            text=f"{album_name}",
            fg="#8B4789"
        )
        
        # Try to load and display the album cover
        image_filename = album_to_image[album_name]
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "album_covers", image_filename)
        
        if os.path.exists(image_path):
            try:
                # Load and resize image
                img = Image.open(image_path)
                img = img.resize((200, 200), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                
                # Update image label
                image_label.config(image=photo)
                image_label.image = photo  # Keep a reference
            except Exception as e:
                image_label.config(image="", text="(Image not available)")
        else:
            image_label.config(image="", text="(Image not found)")
    else:
        messagebox.showerror("Error", "Please enter a valid month name (e.g., January, February, etc.)")

def get_from_dropdown():
    """Get album from dropdown selection"""
    selected = dropdown_var.get()
    if selected and selected != "Select a month...":
        get_taylor_swift_album(selected)
    else:
        messagebox.showerror("Error", "Please select a month from the dropdown")

def get_from_button(month):
    """Get album from month button click"""
    get_taylor_swift_album(month)

# Create main window
root = tk.Tk()
root.title("Taylor Swift Birth Month Album")
root.geometry("800x750")
root.configure(bg="#FFF5F7")

# Load and set background image
script_dir = os.path.dirname(os.path.abspath(__file__))
background_path = os.path.join(script_dir, "album_covers", "background.jpg")

try:
    background_image = Image.open(background_path)
    background_image = background_image.resize((800, 750), Image.Resampling.LANCZOS)
    background_photo = ImageTk.PhotoImage(background_image)
    
    # Create a label for the background
    background_label = tk.Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    pass  # If background image not found, continue without it

# Create a frame for the left side interface (transparent, no border)
left_frame = tk.Frame(root)
left_frame.place(x=20, y=20, width=380, height=710)

# Title label
title_label = tk.Label(
    left_frame,
    text="What is your Taylor Swift\nAlbum?",
    font=("Impact", 22, "bold"),
    fg="#8B4789"
)
title_label.pack(pady=10)

# --- Input Method 1: Text Entry ---
entry_label = tk.Label(
    left_frame,
    text="Option 1: Type your birth month",
    font=("Georgia", 9, "bold"),
    fg="#333333"
)
entry_label.pack(pady=(5, 2))

# Entry field
month_entry = tk.Entry(
    left_frame,
    font=("Georgia", 10, "bold"),
    width=15,
    justify="center"
)
month_entry.pack(pady=2)

# Submit button for text entry
submit_button = tk.Button(
    left_frame,
    text="Find My Album",
    font=("Impact", 12, "bold"),
    bg="#8B4789",
    fg="white",
    command=get_taylor_swift_album,
    cursor="hand2",
    padx=15,
    pady=3
)
submit_button.pack(pady=5)

# --- Input Method 2: Dropdown Menu ---
dropdown_label = tk.Label(
    left_frame,
    text="Option 2: Select from dropdown",
    font=("Georgia", 9, "bold"),
    fg="#333333"
)
dropdown_label.pack(pady=(10, 2))

months_list = ["Select a month...", "January", "February", "March", "April", "May", "June", 
               "July", "August", "September", "October", "November", "December"]
dropdown_var = tk.StringVar(value="Select a month...")
dropdown = ttk.Combobox(
    left_frame,
    textvariable=dropdown_var,
    values=months_list,
    font=("Georgia", 10),
    width=18,
    state="readonly"
)
dropdown.pack(pady=2)

dropdown_button = tk.Button(
    left_frame,
    text="Go",
    font=("Impact", 10, "bold"),
    bg="#8B4789",
    fg="white",
    command=get_from_dropdown,
    cursor="hand2",
    padx=10,
    pady=2
)
dropdown_button.pack(pady=5)

# --- Input Method 3: Month Buttons ---
buttons_label = tk.Label(
    left_frame,
    text="Option 3: Click a month button",
    font=("Georgia", 9, "bold"),
    fg="#333333"
)
buttons_label.pack(pady=(10, 5))

# Create a frame for month buttons
buttons_frame = tk.Frame(left_frame)
buttons_frame.pack(pady=2)

months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

# Create buttons in a 3x4 grid
for i, month in enumerate(months):
    row = i // 3
    col = i % 3
    btn = tk.Button(
        buttons_frame,
        text=month[:3],  # Short name (Jan, Feb, etc.)
        font=("Georgia", 8, "bold"),
        bg="#D8BFD8",
        fg="#333333",
        command=lambda m=month: get_from_button(m),
        cursor="hand2",
        width=6,
        pady=2
    )
    btn.grid(row=row, column=col, padx=3, pady=2)

# Result label
result_label = tk.Label(
    left_frame,
    text="",
    font=("Impact", 18, "bold"),
    fg="#8B4789"
)
result_label.pack(pady=10)

# Image label for album cover
image_label = tk.Label(
    left_frame,
    text=""
)
image_label.pack(pady=10)

# Run the application
root.mainloop()
