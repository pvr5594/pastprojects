import tkinter as tk
from warrior import Warrior
from thief import Thief
from cleric import Cleric
from quiz import Quiz
from phonenix import Phoenix


from dungeon import Dungeon
from sound_fx import SoundFx

from tkinter import *
import re
from mock_game import MockGame as Game


class DungeonAdventure:
    def __init__(self):
        self.__dungeon = None
        self.__hero = None
        self.__monster = None
        self.__diff = 1
        self.__root = tk.Tk()
        self.__window_size = (1150, 875)
        self.__root.geometry(f"{self.__window_size[0]}x{self.__window_size[1]}+250+100")
        self.__root.title("Dungeon Adventure")
        self.__sound = SoundFx()

        self.__intro_slide = 0
        self.__start_canvas = None
        self.__dungeon_display = None
        self.__message_log = None
        self.__legend = None

        self.__omniscience = False
        self.__game_over = False
        self.__make_help_menu()
        self.__initialize_intro()

    def start_loop(self):
        """
        Begins the main loop
        """
        self.__root.mainloop()

    ##################################
    #          GUI methods
    ##################################

    def __initialize_intro(self):
        """
        Sets up canvas for intro slides, then calls the intro method.
        """

        self.__start_canvas = tk.Canvas(self.__root, width=self.__window_size[0], height=self.__window_size[1])
        self.__start_canvas.configure(bg="#000000")

        self.__start_canvas.pack(expand=False)

        self.__root.bind("<Button-1>", self.__advance_intro)

        self.__sound.intro()
        self.__advance_intro(None)

    def __advance_intro(self, keypress): #Replace some of the slides to explain new features/show the names of the new developers
        """
        Each time the method is called, changes the image to create a pseudo-slideshow.
        When the last slide is reached, calls the start menu.
        """
        if self.__intro_slide == 0:
            self.__title_image = tk.PhotoImage(file="assets_intro_1.png")
            self.__start_canvas.create_image(
                self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER, image=self.__title_image)
            self.__intro_slide += 1
        elif self.__intro_slide == 1:
            self.__title_image = tk.PhotoImage(file="assets_intro_2.png")
            self.__start_canvas.create_image(self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER,
                                             image=self.__title_image)
            self.__intro_slide += 1
        elif self.__intro_slide == 2:
            self.__title_image = tk.PhotoImage(file="assets_intro_3.png")
            self.__start_canvas.create_image(self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER,
                                             image=self.__title_image)
            self.__intro_slide += 1
        elif self.__intro_slide == 3:
            self.__title_image = tk.PhotoImage(file="assets_controls.png")
            self.__start_canvas.create_image(self.__window_size[0] // 2, self.__window_size[1] // 2,
                                             anchor=CENTER, image=self.__title_image)
            self.__intro_slide += 1
        elif self.__intro_slide == 4:
            self.__title_image = tk.PhotoImage(file="assets_objectives.png")
            self.__start_canvas.create_image(self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER,
                                             image=self.__title_image)
            self.__intro_slide += 1
        elif self.__intro_slide == 5:
            self.__start_canvas.destroy()
            self.__root.unbind("<Button-1>")
            self.__start_menu()

    def __start_menu(self):
        """
        Creates and displays the start menu.
        """
        if not self.__start_canvas:
            self.__start_canvas = tk.Canvas(self.__root, width=self.__window_size[0], height=self.__window_size[1])
            self.__start_canvas.pack(expand=True)

            self.__title_image = tk.PhotoImage(file="DA_title_bigger.png")
            self.__start_canvas.create_image(self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER,
                                             image=self.__title_image)
        else:
            self.__reset_start_canvas("DA_title_bigger.png")

        # --Buttons
        button_y = self.__window_size[1] // 2 + 240
        button_x = self.__window_size[0] // 2 - 40

        st_menu_button1 = tk.Button(text='Start', font="Verdana 10 bold", width=5)
        self.__start_canvas.create_window(button_x - 260, button_y, window=st_menu_button1)
        st_menu_button1.config(command=self.__choose_class)

        # st_menu_button1.config(command=self.__input_name)

        st_menu_button2 = tk.Button(text='Instruction', font="Verdana 10 bold", width=10)
        self.__start_canvas.create_window(button_x, button_y, window=st_menu_button2)
        st_menu_button2.config(command=self.__display_instructions)

        st_menu_button3 = tk.Button(text='Quit', font="Verdana 10 bold", width=5)
        self.__start_canvas.create_window(button_x + 260, button_y, window=st_menu_button3)
        st_menu_button3.config(command=quit)

    def __start_game(self):
        """
        Sets up the main game interface and binds the controls to enable play.
        """
        self.__reset_start_canvas(None)
        self.__sound.in_game()

        # Setup dungeon & get size
        self.__dungeon = Dungeon(self.__diff, self, self.__hero)
        textbox_size = self.__dungeon.get_size() * 3
        tb_y = self.__window_size[1] // 2

        # build legend textbox
        self.__legend = tk.Text(self.__start_canvas, width=38, height=textbox_size)
        self.__legend.place(x=0, y=tb_y, anchor="w")

        spacer = "\n" * ((textbox_size - 10) // 2)
        self.__legend.insert("end", spacer + "           *****LEGEND***** \n\n    @ = The Adventurer\n    "
                                             "A = pillar of Abstraction\n    E = Pillar of Encapsulation\n    "
                                             "I = Pillar of Inheritance\n    ""P = Pillar of Polymorphism\n    "
                                             "0 = Exit\n    X = Pit (watch out!)\n    H = Health Potion\n    "
                                             "V = Vision Potion\n    B = Both Potions\n    ! = Emu\n    ? = Raven\n"
                                             "    | = Wall")
        self.__legend.config(state="disabled")

        # build dungeon display
        self.__dungeon_display = tk.Text(self.__start_canvas, width=textbox_size, height=textbox_size)
        self.__dungeon_display.place(x=self.__window_size[0] // 2, y=tb_y, anchor=CENTER)

        # build message box
        self.__message_log = tk.Text(self.__start_canvas, width=40, height=textbox_size)
        self.__message_log.place(x=self.__window_size[0], y=tb_y, anchor="e")
        self.__message_log.config(state="disabled")

        self.__draw_map()
        self.announce(self.__hero.__str__())

        # keybinds
        self.__root.bind("<w>", self.__move_player)
        self.__root.bind("<a>", self.__move_player)
        self.__root.bind("<s>", self.__move_player)
        self.__root.bind("<d>", self.__move_player)

        self.__root.bind("<h>", self.__use_health_potion)
        self.__root.bind("<j>", self.__use_vision_potion)
        self.__root.bind("<q>", self.__adventurer_status)

        self.__root.bind("<p>", self.__cheat_codes)
        self.__root.bind("<6>", self.__cheat_codes)
        self.__root.bind("<7>", self.__cheat_codes)
        self.__root.bind("<8>", self.__cheat_codes)
        self.__root.bind("<9>", self.__cheat_codes)
        self.__root.bind("<0>", self.__cheat_codes)

    def __reset_start_canvas(self, file_str):
        """
        Resets the canvas by deleting it and making a fresh one.
        """
        self.__start_canvas.destroy()
        self.__start_canvas = tk.Canvas(self.__root, width=self.__window_size[0], height=self.__window_size[1])
        self.__start_canvas.configure(bg="#000000")
        self.__start_canvas.pack(expand=False)

        if file_str:
            self.__title_image = tk.PhotoImage(file=file_str)
            self.__start_canvas.create_image(self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER,
                                             image=self.__title_image)

    ##################################
    #         Menu Methods
    ##################################
    """Things to do
    Make a new tab that will explain the characteristics of each class, I.E. what stats they'll likely have and there
    special moves"""

    def __make_help_menu(self):
        """
        Creates the help menu and addes it to application menu.
        """
        # --Menu (Help)
        menu_bar = Menu(self.__root)

        filemenu = Menu(menu_bar, tearoff=0)
        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.__root.quit)
        menu_bar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menu_bar, tearoff=0)

        editmenu.add_separator()

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Cheats", command=self.__display_cheats)
        help_menu.add_command(label="Dungeon Key", command=self.__dungeon_key_images)
        help_menu.add_command(label="Help request", command=self.__donothing)
        help_menu.add_command(label="Hero Class Info", command=self.__display_class_info)

        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.__root.config(menu=menu_bar)

    def __donothing(self):
        """
        Taunts the player for daring to ask for help.
        """
        filewin = Toplevel(self.__root)
        button = Button(filewin, text="Help yourself fool!!! \n Read a book or something!!!", font="Verdana 20 bold",
                        width=40)
        button.pack()

    def __display_class_info(self):
        """
        Taunts the player for daring to ask for help.
        """
        filewin = Toplevel(self.__root)
        button = Button(filewin, text="Hello! You have a choice of Three classes to choose from. \n\n"
                                      "Warrior: The warrior has the highest HP, Attack and chance to block. \nThey also"
                                      " have the lowest speed, accuracy and chance to dodge. \nTheir special move is"
                                      " Crushing Blow and deals three times their \nregular damage, but at the cost of"
                                      "it being half their normal accuracy.\n\n"
                                      "Cleric: The cleric has average HP, Attack, Speed, accuracy and \nchance to "
                                      "dodge/block. Their special move is Heal and will restore a \nset amount of HP.\n"
                                      "\nThief: The thief has the lowest HP, Attack and chance to block. \nHowever."
                                      " they have the highest speed, accuracy and chance to dodge.\nTheir special"
                                      " move is sneak attack and it enables the player to attack twice.\nHowever, it "
                                      "only has a 40% chance of success with another 40% \ndelegated to dealing regular"
                                      " damage. The final 20% has a possibility \nof missing entirely.", justify="left",
                        font="Verdana 20 bold",
                        width=65, height=25)
        button.pack()

    def __display_cheats(self):
        """
        Menu option explaining the cheats.
        """
        codes = Toplevel(self.__root)
        button = Button(codes, text="""There are currently seven codes that you can use by typing them on your keyboard 
        (while you are in the maze.) 
        6 = See the whole map (note, this ends as soon as you move) 
        7 = Draw whole map (the whole maze is displayed permanently. (Recommended for people who hate fun)) 
        8 = Increases your health & vision potion count by 50!!! 
        9 = Gives the adventurer all four pillars of OO
        0 = developers hate the player, - 1000 HP. Your Dead
        q = See Adventurer status
        p = Reset the map""", font="Verdana 15 bold",
                        width=90)
        button.pack()

    ##################################
    #         Instantiate hero
    ##################################
    def __choose_class(self):

        # --Buttons
        button_y = self.__window_size[1] // 2 + 240
        button_x = self.__window_size[0] // 2 - 40

        st_menu_button1 = tk.Button(text='Warrior', font="Verdana 10 bold", width=10)
        self.__start_canvas.create_window(button_x - 260, button_y, window=st_menu_button1)
        st_menu_button1.config(command= lambda:self.__input_name("warrior"))

        st_menu_button2 = tk.Button(text='Cleric', font="Verdana 10 bold", width=10)
        self.__start_canvas.create_window(button_x, button_y, window=st_menu_button2)
        st_menu_button2.config(command=lambda: self.__input_name("cleric"))

        st_menu_button3 = tk.Button(text='Thief', font="Verdana 10 bold", width=10)
        self.__start_canvas.create_window(button_x + 260, button_y, window=st_menu_button3)
        st_menu_button3.config(command=lambda: self.__input_name("thief"))

    def __input_name(self, parameter):
        """
        Replaces start menu with entry fields for player name and difficulty.
        """

        "Insures that only numbers can be put in the difficulty textbox"
        def __user_input_adventurer_name():
            difficulty_max_value = 4
            difficulty_min_value = 0

            numbers_only = re.compile("[0-9]*")
            attempt_difficulty = diff.get()
            if numbers_only.fullmatch(attempt_difficulty):
                self.__diff = int(diff.get())
            else:
                print("Use numbers ya goof")
                return

            if difficulty_max_value > int(self.__diff) > difficulty_min_value:
                if parameter == "warrior":
                    self.__hero = Warrior(hero_name.get(), self)
                if parameter == "cleric":
                    self.__hero = Cleric(hero_name.get(), self)
                if parameter == "thief":
                    self.__hero = Thief(hero_name.get(), self)
                self.__reset_start_canvas("assets_background.png")
                # self.combat()
                self.__start_game()
                return

            else:
                print("Please enter a difficulty between 1 and 3.")

        self.__reset_start_canvas("DA_title_bigger.png")

        button_y = self.__window_size[1] // 2 + 240
        button_x = self.__window_size[0] // 2 - 100

        tk.Label(self.__start_canvas,
                 text="Player Name").place(x=button_x - 110, y=button_y - 40)
        tk.Label(self.__start_canvas,
                 text="Difficulty (1-3):").place(x=button_x - 110, y=button_y)

        hero_name = tk.Entry(self.__start_canvas)
        diff = tk.Entry(self.__start_canvas)

        hero_name.place(x=button_x, y=button_y - 40)
        diff.place(x=button_x, y=button_y)

        tk.Button(self.__start_canvas,
                  text='Quit',
                  command=self.__root.destroy).place(x=button_x + 200, y=button_y)

        tk.Button(self.__start_canvas,
                  text='Accept', command=__user_input_adventurer_name).place(x=button_x + 200, y=button_y - 40)

    def __display_instructions(self):
        """
        Gives the player a briefing on how to play the game.
        """
        self.__reset_start_canvas("DA_title_bigger.png")

        tb_x = self.__window_size[0] // 2
        tb_y = self.__window_size[1] // 2
        self.__quiz_text = tk.Text(self.__start_canvas, width=100, height=20)
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
        self.__start_canvas.create_window(button_x, button_y, window=menu_button)
        menu_button.config(command=lambda: self.__start_menu())

    def __dungeon_key_images(self):
        """
        Displays a legend for the dungeon screen.
        """
        dungeon_key = Toplevel(self.__root)
        dungeon_key.title("Dungeon Key")

        button = Button(dungeon_key, text="""Here is the key for images you will find within the dungeon's maze: \n
        @ = The Adventurer
        A = pillar of Abstraction
        E = Pillar of Encapsulation
        I = Pillar of Inheritance
        P = Pillar of Polymorphism
        0 = Exit (Remember that it won't activate until you get all four pillars)
        X = A Pit (removes some HP on enter)
        H = Health Potion (is added into your inventory and removed from room on enter)
        V = Vision Potion (is added into your inventory and removed from room on enter)
        M = Both Potions (is added into your inventory and removed from room on enter)
        " " = Blank Room (nothing to see here move along)
        | = Wall (can't move through this)""", font="Verdana 13 bold", )
        button.pack()

    ##################################
    #      User Keyboard Actions
    ##################################

    def __move_player(self, keypress):
        """
        Passes keyboard input to dungeon to move the player
        """
        if not self.__game_over:
            dir_dict = {
                "w": "n",
                "a": "w",
                "s": "s",
                "d": "e"
            }
            self.__dungeon.move_player(self.__hero, dir_dict[keypress.char])
            self.__hero.decay_vision()

            self.__draw_map()

            if self.__hero.is_dead():
                self.announce(f"{self.__hero.get_name()} has tragically expired.")
                self.end_game()

            if self.__game_over:
                self.__draw_whole_map()

    def __adventurer_status(self, keypress):
        """
        Prints adventurer status to announcements.
        """
        if not self.__game_over:
            self.announce(f"{self.__hero.__str__()}")

    def __use_health_potion(self, keypress):
        """
        Has the adventurer drink a health potion.
        """
        if not self.__game_over:
            self.__hero.use_health_potion()

    def __use_vision_potion(self, keypress):
        """
        Has the adventurer drink a vision potion.
        """
        if not self.__game_over:
            self.__hero.use_vision_potion()
            self.__draw_map()

    def __cheat_codes(self, keypress):
        """
        Enables various cheats when number keys are pressed.
        """
        if not self.__game_over:
            key = keypress.char
            if key == "p":
                self.__start_game()
            if key == "6":
                self.__draw_whole_map()
            elif key == "7":
                self.__omniscience = True
                self.__draw_whole_map()
            elif key == "8":
                for _ in range(0, 50):
                    self.__hero.add_vision_potion()
                    self.__hero.add_health_potion()
            elif key == "9":
                self.__hero.earn_pillar("A")
                self.__hero.earn_pillar("I")
                self.__hero.earn_pillar("E")
                self.__hero.earn_pillar("P")
            elif key == "0":
                self.__hero.take_damage(1000, "the developers")
                self.__draw_whole_map()
                self.end_game()

    ##################################
    #      Game Functionality
    ##################################

    def __draw_map(self):
        """
        Gets the dungeon string from Dungeon and displays it in window
        """
        if not self.__omniscience:
            self.__dungeon_display.config(state="normal")
            self.__dungeon_display.delete("1.0", "end")
            self.__dungeon_display.tag_configure("center", justify="center")
            self.__dungeon_display.insert("1.0", self.__dungeon.display(3, self.__hero.get_vision_range()))
            self.__dungeon_display.tag_add("center", "1.0", "end")
            self.__dungeon_display.config(state="disabled")
        else:
            self.__draw_whole_map()

    def __draw_whole_map(self):
        """
        Prints the entire dungeon to the game window
        """
        self.__dungeon_display.config(state="normal")
        self.__dungeon_display.delete("1.0", "end")
        self.__dungeon_display.insert("1.0", self.__dungeon.__str__(), "center")
        self.__dungeon_display.config(state="disabled")

    def announce(self, message): #change battle log back to announce if no sucess (be sure to fix all classes that changed to self.__announce_battle_log)
        """
        Given a string, prints it to the message log
        """

        log_text = self.__message_log.get("1.0", "end")
        log_text += message
        log_text = log_text.split("\n")

        log_length = self.__dungeon.get_size() * 3 - 5

        if len(log_text) > log_length:
            log_text = log_text[-log_length:]

        log_text = "\n".join(log_text)

        self.__message_log.config(state="normal")
        self.__message_log.delete("1.0", "end")
        self.__message_log.insert("end", log_text)
        self.__message_log.config(state="disabled")

    def end_game(self):
        """
        Ends the game and makes the appropriate announcements.
        """
        self.__game_over = True
        self.announce(self.__hero.__str__())
        if self.__hero.is_dead():
            self.announce("You lose!  Better luck next time!")
        else:
            self.announce("Victory is yours!\nYou have taken the four pillars of object-oriented \nprogramming!")
            self.announce("Without them, the dungeon crumbles behind you.  Whoops!")
