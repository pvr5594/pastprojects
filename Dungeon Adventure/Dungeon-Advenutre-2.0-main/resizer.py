from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Dungeon Adventure")
# root.iconbitmap("c:/gui/codemy.ico")
root.geometry("945x680")

bg = PhotoImage(file="title_screen.png")
my_canvas = Canvas(root, width=940, height=675)

def resizer(e):
    global bg, resized_bg, new_bg
    # Open image
    bg = Image.open("title_screen.png")

    # resize image
    resize_bg = bg.resize((e.width, e.height), Image.ANTIALIAS)

    # define image
    new_bg = ImageTk.PhotoImage(resize_bg)

    # Add back to Canvas
    my_canvas.create_image(0, 0, anchor=NW, image=new_bg)