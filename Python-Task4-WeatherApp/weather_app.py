import tkinter as tk
from tkinter import messagebox
import requests


def get_weather():
    city = city_entry.get()
    if not city or city == "Enter city name":
        messagebox.showerror("Invalid Input", "Please enter a valid city name!")
        return

    # Yahan tumhari API key aa gayi
    api_key = "87c3962fd5fc56ed7ad643223451eebb"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        # Agar data sahi aa gaya (200 OK code)
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"].title()
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            result_label.config(text=f"{temp}°C\n{desc}\n\nHumidity: {humidity}%\nWind: {wind_speed} m/s")

        # Agar API key abhi tak active nahi hui (401 Unauthorized code)
        elif str(data["cod"]) == "401":
            messagebox.showerror("API Error", "API Key is activating... Please wait 10-15 minutes and try again!")

        # Koi aur masla jaise spelling mistake waghaira
        else:
            api_error = data.get("message", "City not found").capitalize()
            messagebox.showerror("Error", f"{api_error}!")

    except Exception as e:
        messagebox.showerror("Error", "Failed to fetch data. Please check your internet connection.")


# UI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("350x450")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

# Fonts & Colors
bg_color = "#1e1e2f"
fg_color = "#ffffff"
btn_color = "#3498db"
font_title = ("Helvetica", 20, "bold")
font_normal = ("Helvetica", 12)
font_large = ("Helvetica", 24, "bold")

# App Header
title_label = tk.Label(root, text="Live Weather", font=font_title, bg=bg_color, fg=btn_color)
title_label.pack(pady=20)

# Search Box
city_entry = tk.Entry(root, font=font_normal, width=20, justify="center", bg="#2c2c3e", fg="#ffffff",
                      insertbackground="white")
city_entry.pack(pady=10, ipady=5)
city_entry.insert(0, "Enter city name")


# Clear placeholder when clicked
def clear_placeholder(event):
    if city_entry.get() == "Enter city name":
        city_entry.delete(0, tk.END)


city_entry.bind("<FocusIn>", clear_placeholder)

# Search Button
search_btn = tk.Button(root, text="Get Weather", font=font_normal, bg=btn_color, fg=fg_color,
                       activebackground="#2980b9", activeforeground="#ffffff", relief="flat", command=get_weather)
search_btn.pack(pady=15, ipadx=10, ipady=2)

# Results Display
result_label = tk.Label(root, text="", font=font_large, bg=bg_color, fg="#2ecc71")
result_label.pack(pady=30)

root.mainloop()
