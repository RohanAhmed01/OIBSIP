import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_var.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4")
            return

        # Combine letters, numbers, and special characters
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))

        password_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def copy_to_clipboard():
    password = password_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to generate first!")

# UI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x450")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

# Fonts & Colors
bg_color = "#1e1e2f"
fg_color = "#ffffff"
btn_color = "#e74c3c"
font_title = ("Helvetica", 20, "bold")
font_normal = ("Helvetica", 12)

# Header
title_label = tk.Label(root, text="Password Generator", font=font_title, bg=bg_color, fg=btn_color)
title_label.pack(pady=20)

# Length Input
length_label = tk.Label(root, text="Select Password Length:", font=font_normal, bg=bg_color, fg=fg_color)
length_label.pack(pady=10)

length_var = tk.IntVar(value=12) # Default length
length_slider = tk.Scale(root, from_=4, to_=32, orient="horizontal", variable=length_var, font=font_normal, bg="#2c2c3e", fg=fg_color, highlightthickness=0, length=200, troughcolor="#1e1e2f")
length_slider.pack(pady=10)

# Generate Button
gen_btn = tk.Button(root, text="Generate Password", font=font_normal, bg=btn_color, fg=fg_color, activebackground="#c0392b", activeforeground="#ffffff", relief="flat", command=generate_password)
gen_btn.pack(pady=20, ipadx=10, ipady=5)

# Password Display
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Helvetica", 14), width=22, justify="center", bg="#2c2c3e", fg="#2ecc71", readonlybackground="#2c2c3e", state="readonly")
password_entry.pack(pady=10, ipady=5)

# Copy Button
copy_btn = tk.Button(root, text="Copy to Clipboard", font=font_normal, bg="#3498db", fg=fg_color, activebackground="#2980b9", activeforeground="#ffffff", relief="flat", command=copy_to_clipboard)
copy_btn.pack(pady=15, ipadx=10, ipady=2)

root.mainloop()
