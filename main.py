import tkinter as tk
from tkinter import messagebox
import random
import json
import os


FONT_NAME = "Lato, serif"
BG_COLOR = "#0b0926"
INPUT_BG_COLOR = "#251f6b"
SUCCESS_COLOR = "#ff5067"

# ---------------------------- GENERATE PASSWORD ------------------------------- #

def generate_password():
    passbox.delete(0, tk.END)

    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_list = (
        [random.choice(letters) for _ in range(random.randint(8, 10))] +
        [random.choice(symbols) for _ in range(random.randint(2, 4))] +
        [random.choice(numbers) for _ in range(random.randint(2, 4))]
    )

    random.shuffle(password_list)
    passbox.insert(0, "".join(password_list))

# ---------------------------- CLEAR ------------------------------- #

def clear_fields():
    sitebox.delete(0, tk.END)
    passbox.delete(0, tk.END)

# ---------------------------- REMOVE LABEL ------------------------------- #

def hide_label():
    message.place_forget()

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = sitebox.get()
    email = emailbox.get()
    password = passbox.get()

    if not website or not password:
        message.config(text="Please fill the form")
    else:
        new_data = {website: {"email": email, "password": password}}

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data.update(new_data)

        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

        message.config(text="Password Added!")
        clear_fields()

    message.place(x=270, y=225)
    window.after(3000, hide_label)  # Hide after 3 seconds

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def find_password():
    website = sitebox.get().strip()

    if not website:
        return messagebox.showerror("Error", "Please enter a website to search")

    if not os.path.exists("data.json") or os.stat("data.json").st_size == 0:
        return messagebox.showerror("Error", "No data found!")

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return messagebox.showerror("Error", "Data file is corrupted!")

    entry = data.get(website)
    if entry:
        messagebox.showinfo("PassMan", f"✅ Found details for {website}!\n\n📧 Email: {entry['email']}\n🔑 Password: {entry['password']}")
    else:
        messagebox.showerror("Not Found!", f"❌ No details found for {website}!")

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=10, bg=BG_COLOR)

# Center the window
WINDOW_WIDTH, WINDOW_HEIGHT = 680, 440
x_pos = (window.winfo_screenwidth() - WINDOW_WIDTH) // 2
y_pos = (window.winfo_screenheight() - WINDOW_HEIGHT) // 2
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_pos}+{y_pos}")

# Canvas for Logo
canvas = tk.Canvas(window, width=250, height=250, bg=BG_COLOR, highlightthickness=0)
try:
    img = tk.PhotoImage(file="logo.png").subsample(3, 3)
    canvas.create_image(127, 127, image=img)
except tk.TclError:
    canvas.create_text(127, 127, text="Logo Missing", fill="white", font=(FONT_NAME, 15, "bold"))
canvas.grid(column=1, row=0, pady=9)

# Success Label
message = tk.Label(window, text=" ", font=(FONT_NAME, 13, "bold"), fg=SUCCESS_COLOR, bg=BG_COLOR)

# Labels & Input Fields
LABEL_CONFIG = {"font": (FONT_NAME, 15, "bold"), "anchor": "w", "bg": BG_COLOR, "fg": "white"}
INPUT_CONFIG = {"width": 45, "bg": INPUT_BG_COLOR, "highlightthickness": 0, "bd": 0}

tk.Label(window, text="Website:", width=16, **LABEL_CONFIG).grid(column=0, row=1, padx=10, pady=1, sticky="w")
sitebox = tk.Entry(window, width=27, bg=INPUT_BG_COLOR, highlightthickness=0, bd=0)
sitebox.focus()
sitebox.grid(column=1, row=1)

tk.Label(window, text="Email | Username:", width=16, **LABEL_CONFIG).grid(column=0, row=2, padx=10, pady=1, sticky="w")
emailbox = tk.Entry(window, **INPUT_CONFIG)
emailbox.insert(0, "ibhxxlz@gmail.com")
emailbox.grid(column=1, row=2, columnspan=2)

tk.Label(window, text="Password:", width=16, **LABEL_CONFIG).grid(column=0, row=3, padx=10, pady=1, sticky="w")
passbox = tk.Entry(window, width=27, bg=INPUT_BG_COLOR, highlightthickness=0, bd=0)
passbox.grid(column=1, row=3)

# Buttons
tk.Button(window, text="Search", font=(FONT_NAME, 13, "bold"), width=14, borderwidth=0, command=find_password, bg="green", fg="black").grid(column=2, row=1)
tk.Button(window, text="Generate Password", font=(FONT_NAME, 13, "bold"), width=14, borderwidth=0, command=generate_password, bg="green", fg="black").grid(column=2, row=3)
tk.Button(window, text="Add", font=(FONT_NAME, 13, "bold"), width=42, borderwidth=0, command=add_password).grid(column=1, row=4, columnspan=2)

# Main Loop
window.mainloop()
