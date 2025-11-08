import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

def get_taylor_swift_album():
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
    
    month_name = month_entry.get().strip()
    
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

# Create main window
root = tk.Tk()
root.title("Taylor Swift Birth Month Album")
root.geometry("800x700")
root.configure(bg="#FFF5F7")

# Load and set background image
script_dir = os.path.dirname(os.path.abspath(__file__))
background_path = os.path.join(script_dir, "album_covers", "background.jpg")

try:
    background_image = Image.open(background_path)
    background_image = background_image.resize((800, 700), Image.Resampling.LANCZOS)
    background_photo = ImageTk.PhotoImage(background_image)
    
    # Create a label for the background
    background_label = tk.Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    pass  # If background image not found, continue without it

# Create a frame for the left side interface (transparent, no border)
left_frame = tk.Frame(root, bg="#FFF5F7")
left_frame.place(x=20, y=50, width=350, height=600)

# Title label
title_label = tk.Label(
    left_frame,
    text="What is your Taylor Swift\nAlbum?",
    font=("Impact", 22, "bold"),
    bg="#FFF5F7",
    fg="#8B4789"
)
title_label.pack(pady=15)

# Instruction label
instruction_label = tk.Label(
    left_frame,
    text="Enter your birth month\n(e.g., January):",
    font=("Georgia", 11, "bold"),
    bg="#FFF5F7",
    fg="#333333"
)
instruction_label.pack(pady=10)

# Entry field
month_entry = tk.Entry(
    left_frame,
    font=("Georgia", 12, "bold"),
    width=15,
    justify="center"
)
month_entry.pack(pady=10)

# Submit button
submit_button = tk.Button(
    left_frame,
    text="Find My Album",
    font=("Impact", 18, "bold"),
    bg="#8B4789",
    fg="white",
    command=get_taylor_swift_album,
    cursor="hand2",
    padx=20,
    pady=5
)
submit_button.pack(pady=15)

# Result label
result_label = tk.Label(
    left_frame,
    text="",
    font=("Impact", 18, "bold"),
    bg="#FFF5F7",
    fg="#8B4789"
)
result_label.pack(pady=10)

# Image label for album cover
image_label = tk.Label(
    left_frame,
    bg="#FFF5F7",
    text=""
)
image_label.pack(pady=10)

# Run the application
root.mainloop()
