import tkinter as tk
from tkinter import *

from sound_fx import SoundFx


class SoundMenu:

    def __init__(self):
        """
        Create instance to pass to DungeonAdventure SoundFx instance, player name & difficulty.
        Start menu.
        """
        self.__root = tk.Tk()
        self.__window_size = (1150, 875)
        self.__root.geometry(f"{self.__window_size[0]}x{self.__window_size[1]}+250+100")
        self.__root.title("Sound Menu")
        self.__title_image = None
        self.__canvas = None
        self.__dungeon_display = None
        self.__message_log = None
        self.change_switch = 'off'

    def sound_menu(self, game_sound, in_game=False):

        self.__canvas = tk.Canvas(self.__root, width=self.__window_size[0], height=self.__window_size[1])
        self.__canvas.configure(bg="#FFBF90")

        self.__canvas.pack(expand=True)

        self.__title_image = tk.PhotoImage(file="DA_title_bigger.png")
        self.__canvas.create_image(self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER,
                                   image=self.__title_image)

        if not game_sound.is_running:
            self.change_switch = 'on'

        button_y = self.__window_size[1] // 2 + 240
        button_x = self.__window_size[0] // 2 - 40

        menu_button1 = tk.Button(text=f'Turn sound on/off', font="Verdana 10 bold", width=15)
        self.__canvas.create_window(button_x, button_y - 400, window=menu_button1)
        menu_button1.config(command=lambda: self.sound_switch(game_sound, in_game))

        menu_button2 = tk.Button(text='Low volume', font="Verdana 10 bold", width=15)
        self.__canvas.create_window(button_x, button_y - 300, window=menu_button2)
        menu_button2.config(command=lambda: game_sound.low_volume())

        menu_button3 = tk.Button(text='Normal volume', font="Verdana 10 bold", width=15)
        self.__canvas.create_window(button_x, button_y - 200, window=menu_button3)
        menu_button3.config(command=lambda: game_sound.normal_volume())

        menu_button4 = tk.Button(text='High volume', font="Verdana 10 bold", width=15)
        self.__canvas.create_window(button_x, button_y - 100, window=menu_button4)
        menu_button4.config(command=lambda: game_sound.high_volume())

        menu_button5 = tk.Button(text='Return', font="Verdana 10 bold", width=15)
        self.__canvas.create_window(button_x, button_y, window=menu_button5)
        menu_button5.config(command=lambda: quit())

        self.__root.mainloop()

    def sound_switch(self, game_sound, in_game):
        if game_sound.is_running:
            game_sound.turn_off()
        else:
            game_sound.turn_on(in_game)
            self.change_switch = 'off'

    def un_sound(self):
        return


if __name__ == "__main__":
    s = SoundMenu()
    ss = SoundFx()
    ss.in_game()
    s.sound_menu(ss, in_game=True)