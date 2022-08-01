import tkinter as tk
from cleric import Cleric
from mock_game import MockGame as Game
from tkinter import *

"""Battleground is activated when a hero walks into a room with a monster"""


class Battleground:
    def __init__(self):
        self.root = tk.Tk()
        self.root.config(bg='#345')
        self.root.title("Combat Mode")
        self.window_size = (1200, 900)
        self.root.geometry(f"{self.window_size[0]}x{self.window_size[1]}+250+100")
        self.__hero = None
        self.__monster = None

    """A GUI that enables the hero to fight the monster. It provides three buttons for three actions. It also has 
    three textbox's, unfortunately they do not connect properly"""

    def combat(self, hero, monster):
        self.__hero = hero
        self.__monster = monster

        start_canvas = tk.Canvas(self.root, width=self.window_size[0], height=self.window_size[1])
        start_canvas.configure(bg="#345")
        start_canvas.pack(expand=False)
        tb_y = self.window_size[1] // 2

        # build Hero textbox
        self.__hero_text = tk.Text(start_canvas, width=42, height=15)
        self.__hero_text.place(x=0, y=tb_y, anchor="w")
        self.__hero_text.insert("end", f"     *****Hero Stats*****    {self.__hero}")

        # build Monster textbox
        self.__monster_text = tk.Text(start_canvas, width=42, height=15)
        self.__monster_text.place(x=self.window_size[0], y=tb_y, anchor="e")
        self.__monster_text.insert("end", f"     *****Monster Stats*****     {self.__monster}")

        # build textbox
        self.__message_log = tk.Text(start_canvas, width=60, height=50)
        self.__message_log.place(x=self.window_size[0] // 2, y=tb_y, anchor=CENTER)
        self.__message_log.insert("end", f"            ")

        # --Buttons
        button_y = self.window_size[1] / 2 + 240
        button_x = self.window_size[0] / 2 - 40

        # Fight Button
        bt_menu_button1 = tk.Button(self.root, text='Fight', font="Verdana 10 bold", width=12)
        start_canvas.create_window(button_x - 450, button_y - 50, window=bt_menu_button1)
        bt_menu_button1.config(command=lambda: self.combat_commands(self.__hero, self.__monster, "Fight"))

        # Special Move Button
        bt_menu_button2 = tk.Button(self.root, text='Special Move', font="Verdana 10 bold", width=12)
        start_canvas.create_window(button_x - 450, button_y, window=bt_menu_button2)
        bt_menu_button2.config(command=lambda: self.combat_commands(self.__hero, self.__monster, "Special Move"))

        # Use Potion Button
        bt_menu_button3 = tk.Button(self.root, text='Use Potion', font="Verdana 10 bold", width=12)
        start_canvas.create_window(button_x - 450, button_y + 50, window=bt_menu_button3)
        bt_menu_button3.config(command=lambda: self.combat_commands(self.__hero, self.__monster, "Potion"))

    """These are the connected commands to the buttons in the above GUI"""
    def combat_commands(self, hero, monster, choice):
        # Fight action
        if choice == "Fight":
            hero.fight(hero, monster)

            if hero.get_current_hp() <= 0 or monster.get_current_hp() <= 0:
                if hero.get_current_hp() <= 0:
                    hero.is_dead()
                    hero.exit()
                self.root.destroy()

        # Special Move action
        elif choice == "Special Move":
            if hero == Cleric(Game, hero.get_name()):
                hero.special_move(hero)
                hero.fight(hero, monster)
            else:
                hero.special_move(monster)
                hero.fight(hero, monster)

            if hero.get_current_hp() <= 0 or monster.get_current_hp() <= 0:
                if hero.get_current_hp() <= 0:
                    hero.is_dead()
                    hero.exit()
                self.root.destroy()

        # Potion action
        elif choice == "Potion":
            hero.use_health_potion()
            hero.fight(hero, monster)
            if hero.get_current_hp() <= 0 or monster.get_current_hp() <= 0:
                if hero.get_current_hp() <= 0:
                    hero.is_dead()
                    hero.exit()
                self.root.destroy()

        tk.mainloop()
