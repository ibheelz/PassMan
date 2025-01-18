import tkinter

window = tkinter.Tk()
window.config(height=1000, width= 1000, padx= 10, pady=10)
window.title("Password Manager")

canvas = tkinter.Canvas(window, width=500, height=500)
img = tkinter.PhotoImage(file= "logo.png")
image = img.subsample(2, 2)
canvas.create_image(250, 150, image=image)
canvas.grid(column=1,row=1)

window.mainloop()