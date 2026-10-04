import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())
        
        if weight <= 0 or height_cm <= 0:
            messagebox.showerror("Invalid Input", "Weight and Height must be positive numbers!")
            return

        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        
        # Determine Category & Color
        if bmi < 18.5:
            category = "Underweight"
            color = "#3498db"  # Blue
        elif 18.5 <= bmi <= 24.9:
            category = "Normal Weight"
            color = "#2ecc71"  # Green
        elif 25 <= bmi <= 29.9:
            category = "Overweight"
            color = "#f1c40f"  # Yellow
        else:
            category = "Obese"
            color = "#e74c3c"  # Red

        # Update UI
        result_label.config(text=f"{bmi:.1f}", fg=color)
        category_label.config(text=category, fg=color)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values!")

# --- UI Setup ---
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x450")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

# Fonts & Colors
bg_color = "#1e1e2f"
fg_color = "#ffffff"
font_title = ("Helvetica", 22, "bold")
font_label = ("Helvetica", 12)
font_entry = ("Helvetica", 14)

# Title
title_label = tk.Label(root, text="BMI Calculator", font=font_title, bg=bg_color, fg="#00e676")
title_label.pack(pady=20)

# Weight Input
tk.Label(root, text="Weight (kg):", font=font_label, bg=bg_color, fg=fg_color).pack(anchor="w", padx=40)
weight_entry = tk.Entry(root, font=font_entry, bg="#2a2a3b", fg=fg_color, insertbackground=fg_color, relief="flat")
weight_entry.pack(fill="x", padx=40, pady=5)

# Height Input
tk.Label(root, text="Height (cm):", font=font_label, bg=bg_color, fg=fg_color).pack(anchor="w", padx=40, pady=(10, 0))
height_entry = tk.Entry(root, font=font_entry, bg="#2a2a3b", fg=fg_color, insertbackground=fg_color, relief="flat")
height_entry.pack(fill="x", padx=40, pady=5)

# Calculate Button
calc_btn = tk.Button(root, text="Calculate BMI", font=("Helvetica", 14, "bold"), bg="#00e676", fg="#1e1e2f", 
                     activebackground="#00c853", activeforeground="#1e1e2f", relief="flat", command=calculate_bmi)
calc_btn.pack(fill="x", padx=40, pady=30)

# Results Display
tk.Label(root, text="Your BMI:", font=font_label, bg=bg_color, fg="#a0a0b0").pack()
result_label = tk.Label(root, text="0.0", font=("Helvetica", 36, "bold"), bg=bg_color, fg=fg_color)
result_label.pack()

category_label = tk.Label(root, text="Enter details", font=("Helvetica", 14, "italic"), bg=bg_color, fg="#a0a0b0")
category_label.pack(pady=5)

root.mainloop()