import tkinter as tk
from tkinter import messagebox
import math


class CircleAreaCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Circle Area Calculator")
        self.root.geometry("400x250")
        self.root.resizable(False, False)
        
        # Create and configure the main frame
        main_frame = tk.Frame(root, padx=20, pady=20)
        main_frame.pack(expand=True)
        
        # Title label
        title_label = tk.Label(
            main_frame,
            text="Circle Area Calculator",
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=(0, 20))
        
        # Radius input frame
        input_frame = tk.Frame(main_frame)
        input_frame.pack(pady=10)
        
        radius_label = tk.Label(
            input_frame,
            text="Enter Radius:",
            font=("Arial", 12)
        )
        radius_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.radius_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            width=15
        )
        self.radius_entry.pack(side=tk.LEFT)
        self.radius_entry.bind('<Return>', lambda event: self.calculate_area())
        
        # Calculate button
        calculate_button = tk.Button(
            main_frame,
            text="Calculate Area",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
            command=self.calculate_area
        )
        calculate_button.pack(pady=15)
        
        # Result label
        self.result_label = tk.Label(
            main_frame,
            text="",
            font=("Arial", 12),
            fg="#2196F3"
        )
        self.result_label.pack(pady=10)
        
        # Focus on entry field
        self.radius_entry.focus()
    
    def calculate_area(self):
        try:
            # Get the radius from the entry field
            radius_str = self.radius_entry.get().strip()
            
            if not radius_str:
                messagebox.showwarning("Input Error", "Please enter a radius value.")
                return
            
            radius = float(radius_str)
            
            if radius < 0:
                messagebox.showerror("Invalid Input", "Radius cannot be negative.")
                return
            
            # Calculate the area
            area = math.pi * radius ** 2
            
            # Display the result
            self.result_label.config(
                text=f"Area = {area:.2f} square units",
                fg="#2196F3"
            )
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid numeric value.")
            self.radius_entry.delete(0, tk.END)
            self.radius_entry.focus()


def main():
    root = tk.Tk()
    app = CircleAreaCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
