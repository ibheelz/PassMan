import tkinter
FONT_NAME = "lato"


# ---------------------------- CLEAR ------------------------------- #

def clear():
    sitebox.delete(0, tkinter.END)
    passbox.delete(0, tkinter.END)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website_data = sitebox.get()
    email_data = mailbox.get()
    password_data = passbox.get()
    data = open("data.txt", "a")
    data.write(f"{website_data} | {email_data} | {password_data} \n")
    data.close()
    clear()

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.config(padx=20, pady=10, bg="#0b0926")
window.title("Password Manager")

# Define the window width and height
window_width = 680  # Adjust this to your preferred width
window_height = 440  # Adjust this to your preferred height

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the position for the window to be centered
x_pos = (screen_width - window_width) // 2
y_pos = (screen_height - window_height) // 2

# Set the geometry of the window (Width x Height + X_position + Y_position)
window.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

# Adding image to the canvas
canvas = tkinter.Canvas(window, width=250, height=250, bg="#0b0926", highlightthickness=0)
img = tkinter.PhotoImage(file="logo.png")
image = img.subsample(3, 3)
canvas.create_image(127, 127, image=image)
canvas.grid(column=1, row=0, pady=9)

# Label and Entry configuration
label_width = 20  # Set a common width for all labels and entry boxes
entry_width = 45  # Entry boxes width

# Website Label and Entry
website = tkinter.Label(window, text="Website:", font=(FONT_NAME, 15, "bold"), width=label_width, anchor="w", bg="#0b0926", fg="white")
website.grid(column=0, row=1, padx=10, pady=1, sticky="w")

sitebox = tkinter.Entry(window, width=entry_width, bg="#251f6b", highlightthickness=0, bd=0)
sitebox.focus()
sitebox.grid(column=1, row=1, columnspan=2, pady=1)

# mail Label and Entry
email = tkinter.Label(window, text="Email | Username:", font=(FONT_NAME, 15, "bold"), width=label_width, anchor="w", bg="#0b0926", fg="white")
email.grid(column=0, row=2, padx=10, pady=1, sticky="w")

mailbox = tkinter.Entry(window, width=entry_width, bg="#251f6b", highlightthickness=0, bd=0)
mailbox.insert(0, "ibhxxlz@gmail.com")
mailbox.grid(column=1, row=2, columnspan=2, pady=1)

# Password Label and Entry
password = tkinter.Label(window, text="Password:", font=(FONT_NAME, 15, "bold"), width=label_width, anchor="w", bg="#0b0926", fg="white")
password.grid(column=0, row=3, padx=10, pady=1, sticky="w")

passbox = tkinter.Entry(window, width=25, bg="#251f6b", highlightthickness=0, bd=0)
passbox.grid(column=1, row=3, pady=5)

# Password Generation Button
generate = tkinter.Button(window, text="Generate Password", font=(FONT_NAME, 13, "bold"), width=14, borderwidth=0, bg="green", fg="black")
generate.grid(column=2, row=3, padx=10, pady=1)

# Add Button
add = tkinter.Button(window, text="Add", font=(FONT_NAME, 13, "bold"), width=42, borderwidth=0, command=add_password)
add.grid(column=1, row=4, columnspan=2, pady=1)



# Running the main loop
window.mainloop()
