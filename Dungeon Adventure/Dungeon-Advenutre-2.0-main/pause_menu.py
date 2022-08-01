from sound_menu import SoundMenu
import tkinter as tk
from tkinter import *
from sound_fx import SoundFx


class PauseMenu:

    def __init__(self):
        """
        Create instance to pass to DungeonAdventure SoundFx instance, player name & difficulty.
        Start menu.
        """
        self.__root = tk.Tk()
        self.__window_size = (1150, 875)
        self.__root.geometry(f"{self.__window_size[0]}x{self.__window_size[1]}+250+100")
        self.__root.title("Pause Menu")
        self.__instr_slide = 0
        self.__canvas = None
        self.__dungeon_display = None
        self.__message_log = None

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

    def resume(self, r):
        if r == 'True':
            return True
        else:
            return False

    def intro(self, game_sound):
        """
        Sets up canvas for intro slides, then calls the intro method.
        """

        self.__canvas = tk.Canvas(self.__root, width=self.__window_size[0], height=self.__window_size[1])
        self.__canvas.configure(bg="#FFBF90")

        self.__canvas.pack(expand=True)

        self.__menu(game_sound)

    def __menu(self, game_sound):

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

        snd = SoundMenu()

        menu_button1 = tk.Button(text='Resume', font="Verdana 10 bold", width=15)
        self.__canvas.create_window(button_x, button_y - 400, window=menu_button1)
        menu_button1.config(command=lambda: self.resume('False'))

        menu_button2 = tk.Button(text='Instruction', font="Verdana 10 bold", width=15)
        self.__canvas.create_window(button_x, button_y - 300, window=menu_button2)
        menu_button2.config(command=lambda: self.__instructions(game_sound))

        menu_button3 = tk.Button(text='Sound Menu', font="Verdana 10 bold", width=15)
        self.__canvas.create_window(button_x, button_y - 200, window=menu_button3)
        menu_button3.config(command=lambda: snd.sound_menu(game_sound, in_game=True))

        menu_button4 = tk.Button(text='Quit', font="Verdana 10 bold", width=15)
        self.__canvas.create_window(button_x, button_y - 100, window=menu_button4)
        menu_button4.config(command=lambda: quit())

        self.__root.mainloop()

    def __instructions(self, game_sound):
        self.__reset_menu_canvas("DA_title_bigger.png")

        tb_x = self.__window_size[0] // 2
        tb_y = self.__window_size[1] // 2
        self.__quiz_text = tk.Text(self.__canvas, width=100, height=20)
        self.__quiz_text.place(x=tb_x, y=tb_y, anchor=CENTER)

        self.__quiz_text.insert("end", "Hello! You have a choice of Three classes to choose from. \n\n"
                                       "Warrior: The warrior has the highest HP, Attack and chance to block. \nThey "
                                       "also "
                                       " have the lowest speed, accuracy and chance to dodge. \nTheir special move is"
                                       " Crushing Blow and deals three times their \nregular damage, but at the cost of"
                                       "it being half their normal accuracy.\n\n"
                                       "Cleric: The cleric has average HP, Attack, Speed, accuracy and \nchance to "
                                       "dodge/block. Their special move is Heal and will restore a \nset amount of "
                                       "HP.\n "
                                       "\nThief: The thief has the lowest HP, Attack and chance to block. \nHowever."
                                       " they have the highest speed, accuracy and chance to dodge.\nTheir special"
                                       " move is sneak attack and it enables the player to attack twice.\nHowever, it "
                                       "only has a 40% chance of success with another 40% \ndelegated to dealing "
                                       "regular "
                                       " damage. The final 20% has a possibility \nof missing entirely.")

        button_y = self.__window_size[1] // 2 + 240
        button_x = self.__window_size[0] // 2 - 40

        menu_button = tk.Button(text='Continue', font="Verdana 10 bold", width=10)
        self.__canvas.create_window(button_x, button_y, window=menu_button)
        menu_button.config(command=lambda: self.__menu(game_sound))


if __name__ == "__main__":
    s = PauseMenu()
    sound = SoundFx()
    sound.intro()
    s.intro(sound)
