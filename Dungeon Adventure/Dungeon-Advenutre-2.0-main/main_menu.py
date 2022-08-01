from sound_fx import SoundFx
# from sound_menu import SoundOption
import tkinter as tk
from tkinter import *
# import re
from dungeon_adventure import DungeonAdventure


class MainMenu:
    """
    This runs the main menu, through which the user can access the game, read instructions for the game, adjust sound
    options or exit the game.
    """

    def __init__(self):
        """
        Create instance to pass to DungeonAdventure SoundFx instance, player name & difficulty.
        Start menu.
        """
        self.__root = tk.Tk()
        self.__window_size = (1150, 875)
        self.__root.geometry(f"{self.__window_size[0]}x{self.__window_size[1]}+250+100")
        self.__root.title("Main Menu")
        self.__instr_slide = 0
        self.__canvas = None
        self.__dungeon_display = None
        self.__message_log = None
        self.__sound = SoundFx()
        self.__intro()

    def start_loop(self):
        """
        Begins the main loop
        """
        self.__root.mainloop()

    @property
    def sound(self):
        """
        Getter for sound
        :return: obtain user's instance of SoundFx
        :rtype: SoundFx
        """
        return self.__sound

    def __reset_menu_canvas(self, file_str):
        """
        Resets the canvas by deleting it and making a fresh one.
        """
        self.__canvas.destroy()
        self.__canvas = tk.Canvas(self.__root, width=self.__window_size[0], height=self.__window_size[1])
        self.__canvas.configure(bg="#FFBF90")
        self.__canvas.pack(expand=True)

        if file_str:
            self.__image = tk.PhotoImage(file=file_str)
            self.__canvas.create_image(self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER,
                                       image=self.__image)

    def __intro(self):
        """
        Sets up canvas for intro slides, then calls the intro method.
        """

        self.__canvas = tk.Canvas(self.__root, width=self.__window_size[0], height=self.__window_size[1])
        self.__canvas.configure(bg="#FFBF90")

        self.__canvas.pack(expand=True)

        self.__menu()

    def __menu(self):

        new_adventure = DungeonAdventure()

        if not self.__canvas:
            self.__canvas = tk.Canvas(self.__root, width=self.__window_size[0], height=self.__window_size[1])
            self.__canvas.pack(expand=True)

            self.__title_image = tk.PhotoImage(file="tDA_title_bigger.png")
            self.__canvas.create_image(self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER,
                                       image=self.__title_image)
        else:
            self.__reset_menu_canvas("DA_title_bigger.png")

        button_y = self.__window_size[1] // 2 + 240
        button_x = self.__window_size[0] // 2 - 40

        menu_button1 = tk.Button(text='Start', font="Verdana 10 bold", width=5)
        self.__canvas.create_window(button_x - 260, button_y, window=menu_button1)
        menu_button1.config(command=lambda: new_adventure.start_loop())

        menu_button2 = tk.Button(text='Instruction', font="Verdana 10 bold", width=10)
        self.__canvas.create_window(button_x, button_y, window=menu_button2)
        menu_button2.config(command=lambda: self.__instructions(None))

        menu_button3 = tk.Button(text='Quit', font="Verdana 10 bold", width=5)
        self.__canvas.create_window(button_x + 260, button_y, window=menu_button3)
        menu_button3.config(command=lambda: quit())

    # def __choose_class(self):
    #
    #     self.__reset_menu_canvas("DA_title_bigger.png")
    #
    #     button_y = self.__window_size[1] // 2 + 240
    #     button_x = self.__window_size[0] // 2 - 40
    #
    #     st_menu_button1 = tk.Button(text='Warrior', font="Verdana 10 bold", width=10)
    #     self.__canvas.create_window(button_x - 260, button_y, window=st_menu_button1)
    #     st_menu_button1.config(command=lambda: self.__input_name("warrior"))
    #
    #     st_menu_button2 = tk.Button(text='Cleric', font="Verdana 10 bold", width=10)
    #     self.__canvas.create_window(button_x, button_y, window=st_menu_button2)
    #     st_menu_button2.config(command=lambda: self.__input_name("cleric"))
    #
    #     st_menu_button3 = tk.Button(text='Thief', font="Verdana 10 bold", width=10)
    #     self.__canvas.create_window(button_x + 260, button_y, window=st_menu_button3)
    #     st_menu_button3.config(command=lambda: self.__input_name("thief"))

    def __instructions(self, keypress):
        self.__reset_menu_canvas("assets_title.png")

        self.__root.bind("<Button-1>", self.__instructions)

        if self.__instr_slide == 0:
            self.__title_image = tk.PhotoImage(file="assets_intro_1.png")
            self.__canvas.create_image(
                self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER, image=self.__title_image)
            self.__instr_slide += 1
        elif self.__instr_slide == 1:
            self.__title_image = tk.PhotoImage(file="assets_intro_2.png")
            self.__canvas.create_image(
                self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER, image=self.__title_image)
            self.__instr_slide += 1
        elif self.__instr_slide == 2:
            self.__title_image = tk.PhotoImage(file="assets_intro_3.png")
            self.__canvas.create_image(
                self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER, image=self.__title_image)
            self.__instr_slide += 1
        elif self.__instr_slide == 3:
            self.__title_image = tk.PhotoImage(file="assets_controls.png")
            self.__canvas.create_image(
                self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER, image=self.__title_image)
            self.__instr_slide += 1
        elif self.__instr_slide == 4:
            self.__title_image = tk.PhotoImage(file="assets_objectives.png")
            self.__canvas.create_image(
                self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER, image=self.__title_image)
            self.__instr_slide += 1
        elif self.__instr_slide == 5:
            self.__root.unbind("<Button-1>")
            self.__canvas.destroy()
            self.__menu()

