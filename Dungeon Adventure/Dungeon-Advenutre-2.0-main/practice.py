from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Dungeon Adventure")
# root.iconbitmap("c:/gui/codemy.ico")
root.geometry("945x680")

bg = PhotoImage(file="title.png")
my_canvas = Canvas(root, width=940, height=675)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0, 0, image=bg, anchor=NW)


button1 = Button(root, text="Start")
button2 = Button(root, text="Instruction")
button3 = Button(root, text="Quit")

button1_window = my_canvas.create_window(650, 500, anchor="nw", window=button1)
button2_window = my_canvas.create_window(650, 530, anchor="nw", window=button2)
button3_window = my_canvas.create_window(650, 560, anchor="nw", window=button3)


def resizer(e):
    global bg1, resized_bg, new_bg
    # Open image
    bg1 = Image.open("title.png")

    # resize image
    resize_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)

    # define image
    new_bg = ImageTk.PhotoImage(resize_bg)

    # Add back to Canvas
    my_canvas.create_image(0, 0, anchor=NW, image=new_bg)


root.bind('<Configure>', resizer)
root.mainloop()


