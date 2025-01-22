import tkinter as tk

FONT_NAME = "Lato"
BG_COLOR = "#0b0926"
INPUT_BG_COLOR = "#251f6b"
SUCCESS_COLOR = "#ff5067"

# ---------------------------- CLEAR ------------------------------- #
def clear_fields():
    """Clear the sitebox and passbox fields."""
    sitebox.delete(0, tk.END)
    passbox.delete(0, tk.END)

# ---------------------------- REMOVE LABEL ------------------------------- #
def hide_label():
    """Hide the success label."""
    success.place_forget()

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    """Save the entered website, email, and password to a file."""
    website = sitebox.get()
    email = mailbox.get()
    password = passbox.get()

    if not website or not password:
        success.config(text="Fill the form")
    else:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
        success.config(text="Password Added!")
        clear_fields()

    success.place(x=277, y=225)  # Show the success message
    window.after(3000, hide_label)  # Hide it after 3 seconds

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=10, bg=BG_COLOR)

# Center the window on the screen
WINDOW_WIDTH, WINDOW_HEIGHT = 680, 440
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_pos = (screen_width - WINDOW_WIDTH) // 2
y_pos = (screen_height - WINDOW_HEIGHT) // 2
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_pos}+{y_pos}")

# Add logo to the canvas
canvas = tk.Canvas(window, width=250, height=250, bg=BG_COLOR, highlightthickness=0)
try:
    img = tk.PhotoImage(file="logo.png").subsample(3, 3)
    canvas.create_image(127, 127, image=img)
except tk.TclError:
    canvas.create_text(127, 127, text="Logo Missing", fill="white", font=(FONT_NAME, 15, "bold"))
canvas.grid(column=1, row=0, pady=9)

# Success Label
success = tk.Label(window, text=" ", font=(FONT_NAME, 13, "bold"), fg=SUCCESS_COLOR, bg=BG_COLOR)

# Field Labels and Input Configuration
LABEL_CONFIG = {"font": (FONT_NAME, 15, "bold"), "anchor": "w", "bg": BG_COLOR, "fg": "white"}
INPUT_CONFIG = {"width": 45, "bg": INPUT_BG_COLOR, "highlightthickness": 0, "bd": 0}

# Website
tk.Label(window, text="Website:", width=20, **LABEL_CONFIG).grid(column=0, row=1, padx=10, pady=1, sticky="w")
sitebox = tk.Entry(window, **INPUT_CONFIG)
sitebox.focus()
sitebox.grid(column=1, row=1, columnspan=2, pady=1)

# Email
tk.Label(window, text="Email | Username:", width=20, **LABEL_CONFIG).grid(column=0, row=2, padx=10, pady=1, sticky="w")
mailbox = tk.Entry(window, **INPUT_CONFIG)
mailbox.insert(0, "ibhxxlz@gmail.com")
mailbox.grid(column=1, row=2, columnspan=2, pady=1)

# Password
tk.Label(window, text="Password:", width=20, **LABEL_CONFIG).grid(column=0, row=3, padx=10, pady=1, sticky="w")
passbox = tk.Entry(window, width=25, bg=INPUT_BG_COLOR, highlightthickness=0, bd=0)
passbox.grid(column=1, row=3, pady=5)

# Buttons
tk.Button(
    window, text="Generate Password", font=(FONT_NAME, 13, "bold"), width=14, borderwidth=0, bg="green", fg="black"
).grid(column=2, row=3, padx=10, pady=1)
tk.Button(
    window, text="Add", font=(FONT_NAME, 13, "bold"), width=42, borderwidth=0, command=add_password
).grid(column=1, row=4, columnspan=2, pady=1)

# Main Loop
window.mainloop()
