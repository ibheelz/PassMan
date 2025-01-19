import tkinter
from tkinter.ttk import Label

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.config(height=1000, width=1000, padx=50, pady=50)
window.title("Password Manager")

# Adding image to the canvas
canvas = tkinter.Canvas(window, width=250, height=250)
img = tkinter.PhotoImage(file="logo.png")
image = img.subsample(2, 2)
canvas.create_image(127, 127, image=image)
canvas.grid(column=1, row=0, pady=30)

# Label and Entry configuration
label_width = 20  # Set a common width for all labels and entry boxes
entry_width = 45  # Entry boxes width

# Website Label and Entry
website = Label(window, text="Website:", width=label_width, anchor="w")
website.grid(column=0, row=1, padx=10, pady=5, sticky="w")

textbox1 = tkinter.Entry(window, width=entry_width)
textbox1.grid(column=1, row=1, columnspan=2, pady=5)

# Email Label and Entry
email = Label(window, text="Email | Username:", width=label_width, anchor="w")
email.grid(column=0, row=2, padx=10, pady=5, sticky="w")

textbox2 = tkinter.Entry(window, width=entry_width)
textbox2.grid(column=1, row=2, columnspan=2, pady=5)

# Password Label and Entry
password = Label(window, text="Password:", width=label_width, anchor="w")
password.grid(column=0, row=3, padx=10, pady=5, sticky="w")

textbox3 = tkinter.Entry(window, width=25)
textbox3.grid(column=1, row=3, pady=5)

# Password Generation Button
button1 = tkinter.Button(window, text="Generate Password", width=14)
button1.grid(column=2, row=3, padx=10, pady=5)

# Add Button
button2 = tkinter.Button(window, text="Add", width=43)
button2.grid(column=1, row=4, columnspan=2, pady=5)

# Running the main loop
window.mainloop()

