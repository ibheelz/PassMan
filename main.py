import tkinter
from cProfile import label
from tkinter.ttk import Label

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.config(height=1000, width= 1000, padx= 50, pady=50)
window.title("Password Manager")

canvas = tkinter.Canvas(window, width=200, height=200)
img = tkinter.PhotoImage(file= "logo.png")
image = img.subsample(2, 2)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1,row=1)

website = Label(text="Website:")
website.grid(column=0, row=2)

email = Label(text="Email | Username:")
email.grid(column=0, row=3)

password = Label(text="Password:")
password.grid(column=0, row=4)


window.mainloop()