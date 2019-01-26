import random
from tkinter import *
from PIL import Image, ImageTk

def rolling():
    random_number = random.randrange(1,7)
    rolled.set(random_number)
    # t1.delete("1.0", END)
    # t1.insert(END, random_number, "center")

window = Tk()
window.title("Dice")
window.geometry("210x210")
window.resizable(0,0)
load = Image.open("dice.png")
image = ImageTk.PhotoImage(load)
img = Label(image=image)
img.place(x=20, y=20)


b1 = Button(window, text="Roll!", width= 10, command = rolling)
b1.grid(row=0, column=0)

rolled = StringVar()
l2 = Label(window, textvariable = rolled, width= 5)
l2.grid(row = 0, column=2)
l2.configure(font=40)
# t1 = Text(window, height=1, width=7)
# t1.grid(row=1, column=0)
# t1.config(font=(44))
# t1.tag_configure("center", justify="center")



window.mainloop()
