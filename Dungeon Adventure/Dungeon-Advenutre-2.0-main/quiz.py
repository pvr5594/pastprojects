import tkinter as tk
from sqlite_creation import Connect
from sqliteinsert import Insert
from sqliteupdate import Update
from sqliteselect import Select
import random
from tkinter import *
from battleground import Battleground


class Quiz:
    def __init__(self):
        self.sqlite_creation = Connect()
        self.sqlite_insert = Insert()
        self.sqlite_update = Update()
        self.sqlite_select = Select()
        self.__root = tk.Tk()
        self.__window_size = (1150, 875)
        self.__root.geometry(f"{self.__window_size[0]}x{self.__window_size[1]}+250+100")
        self.__root.title("Sphinx Death Quiz")
        self.__canvas = None
        self.__image = None
        self.__text = None
        self.__quiz_text = None
        self.__row = None
        self.__question = None
        self.__quiz = None
        self.__answer = None
        self.grade = None

    def __reset_start_canvas(self, file_str):
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

    def create(self):
        """
        Creates a quiz table and database file
        :return: None
        """
        database = r"dungeonquiz.db"
        sql_create_questions_table = """ CREATE TABLE IF NOT EXISTS quiz (
                                        id integer PRIMARY KEY,
                                        category text NOT NULL,
                                        question text NOT NULL,
                                        answer text NOT NULL
                                    ); """

        conn = self.sqlite_creation.create_connection(database)

        if conn is not None:
            self.sqlite_creation.create_table(conn, sql_create_questions_table)
        else:
            print("Error! cannot create the database connection.")

    def insert(self, category, question, answer):
        """
        Insert data for a quiz question
        :param category: the category of the quiz question
        :param question: the quiz question itself
        :param answer: the answer of the question
        :return: None
        """
        database = r"dungeonquiz.db"

        conn = self.sqlite_insert.create_connection(database)
        with conn:
            question = (category, question, answer)
            self.sqlite_insert.create_question(conn, question)

    def update(self, id, category, question, answer):
        """
        updates a question in the table
        :param id: the id of the question to be updated
        :param category: new category input
        :param question: new question input
        :param answer: new answer input
        :return: None
        """
        database = r"dungeonquiz.db"

        conn = self.sqlite_update.create_connection(database)
        with conn:
            self.sqlite_update.update_task(conn, (id, category, question, answer))

        print('done')

    def select(self, category):
        """
        selects a specific question from the db based on the category provided
        :param category: the provided category
        :return: the row selected based on the provided category
        """
        database = r"dungeonquiz.db"

        conn = self.sqlite_select.create_connection(database)
        with conn:
            if category == 'Abstraction':
                q_id = str(random.randrange(1, 5))
                self.__row = self.sqlite_select.selected_quiz(self.sqlite_select.select_quiz_by_priority(conn, q_id))
            elif category == 'Encapsulation':
                q_id = str(random.randrange(6, 10))
                self.__row = self.sqlite_select.selected_quiz(self.sqlite_select.select_quiz_by_priority(conn, q_id))
            elif category == 'Inheritance':
                q_id = str(random.randrange(11, 15))
                self.__row = self.sqlite_select.selected_quiz(self.sqlite_select.select_quiz_by_priority(conn, q_id))
            elif category == 'Polymorphism':
                q_id = str(random.randrange(16, 20))
                self.__row = self.sqlite_select.selected_quiz(self.sqlite_select.select_quiz_by_priority(conn, q_id))

        return self.__row

    def start_quiz(self, category, hero, monster):
        """
        Starts the quiz GUI and displays the question selected and buttons to select an answer
        :param category: category of quiz question to be selected
        :param hero: the player character date (in case battle is initiated)
        :param monster: monster date (in case battle is initiated)
        :return: the player's answer to the quiz question provided
        """
        self.select(category)
        self.__question = self.__row[2]
        self.__answer = self.__row[3]

        self.__canvas = tk.Canvas(self.__root, width=self.__window_size[0], height=self.__window_size[1])
        self.__canvas.pack(expand=True)

        # self.__image = tk.PhotoImage(file="assets_background.png")
        # self.__canvas.create_image(self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER,
        #                            image=self.__image)

        tb_x = self.__window_size[0] // 2
        tb_y = self.__window_size[1] // 2

        self.__quiz_text = tk.Text(self.__canvas, width=100, height=10)
        self.__quiz_text.place(x=tb_x, y=tb_y, anchor=CENTER)

        self.__quiz_text.insert("end", self.__question)

        button_y = self.__window_size[1] // 2 + 240
        button_x = self.__window_size[0] // 2 - 40

        button1 = tk.Button(self.__root, text='True', font="Verdana 10 bold", width=5)
        self.__canvas.create_window(button_x - 260, button_y, window=button1)
        button1.config(command=lambda: self.quiz_answer('True', self.__answer, hero, monster))

        button2 = tk.Button(self.__root, text='False', font="Verdana 10 bold", width=10)
        self.__canvas.create_window(button_x, button_y, window=button2)
        button2.config(command=lambda: self.quiz_answer('False', self.__answer, hero, monster))

        button3 = tk.Button(self.__root, text='I am Stupid', font="Verdana 10 bold", width=10)
        self.__canvas.create_window(button_x + 260, button_y, window=button3)
        button3.config(command=lambda: self.quiz_answer('Dumb', self.__answer, hero, monster))

        self.__root.mainloop()

    def quiz_answer(self, my_ans, cor_ans, hero, monster):
        """
        Determines a grade based on the player's answer
        :param my_ans: the player's answer to the quiz question
        :param cor_ans: the provided 'correct' answer
        :param hero: the player character date (in case battle is initiated)
        :param monster: monster date (in case battle is initiated)
        :return: self.grade; boolean
        """
        self.__reset_start_canvas("")

        tb_x = self.__window_size[0] // 2
        tb_y = self.__window_size[1] // 2
        self.__text = tk.Text(self.__canvas, width=50, height=20)
        self.__text.place(x=tb_x, y=tb_y, anchor=CENTER)

        if my_ans == 'Dumb':
            self.__text.insert("end", "You ara a Dumbass! Prepare to Die!!")
            self.grade = False

        elif my_ans == cor_ans:
            self.__text.insert("end", "You have answered correctly. Well Done.")
            self.grade = True

        else:
            self.__text.insert("end", "You have answered incorrectly. Prepare to Die!")
            self.grade = False

        button_y = self.__window_size[1] // 2 + 240
        button_x = self.__window_size[0] // 2 - 40

        button = tk.Button(self.__root, text='Continue', font="Verdana 10 bold", width=10)
        self.__canvas.create_window(button_x, button_y, window=button)
        button.config(command=lambda: self.quiz_grade(self.grade, hero, monster))

    def quiz_grade(self, grade, hero, monster):
        """
        Either does nothing or enters combat based on the player's grade
        :param grade: the player's grade (indicates a correct or incorrect response)
        :param hero: the player character date (in case battle is initiated)
        :param monster: monster date (in case battle is initiated)
        :return: either do nothing or transfers to battle based on player grade
        """
        if grade:
            pass
        else:
            battle = Battleground()
            battle.combat(hero, monster)
        self.__root.destroy()


# if __name__ == "__main__":
#     q = Quiz()
#     q.create()
#     q.insert('Abstraction', 'Abstraction is used to represent a specific entity in your object-oriented solution. It '
#                             'is composed of attributes and behaviors. You do not worry about the details of how '
#                             'things are represented ("Spare me the details"). The fundamental unit of this pillar is '
#                             'a class.', 'True')
#     q.insert('Abstraction', 'An abstract class cannot have instance data or non-abstract methods.', 'False')
#     q.insert('Abstraction', 'Attempting to instantiate an object of an abstract class is a logic error.', 'False')
#     q.insert('Abstraction', 'An abstract class declares a common interface for the various members of a class '
#                             'hierarchy. The abstract class contains methods that will be declared in the subclasses. '
#                             'All classes in the hierarchy can use this same set of methods through polymorphism.', 'True')
#     q.insert('Abstraction', 'Objects of abstract superclasses can be instantiated.', 'False')
#     q.insert('Encapsulation', 'Encapsulation is concerned with data hiding and keeping the inner workings of the '
#                               'class restricted to the outside world (other objects from other classes).It '
#                               'effectively says, "None of your darned business."', 'True')
#     q.insert('Encapsulation', 'Private members of a class cannot be accessed.', 'False')
#     q.insert('Encapsulation', 'The purpose of name mangling is to avoid unintentional access of private class members.', 'True')
#     q.insert('Encapsulation', 'While using encapsulation, data member’s data type can be changed without changing any '
#                               'other code.', 'True')
#     q.insert('Encapsulation', 'With encapsulation it’s difficult to change and adapt to new requirements.', 'False')
#     q.insert('Inheritance', 'Inheritance allows you to build a more specific version of a general class. It is a '
#                             'white box approach to design and thus violates encapsulation principles. It is '
#                             'characterized as an "is-a" relationship.', 'True')
#     q.insert('Inheritance', 'An interface is typically used in place of an abstract class when there is no default '
#                             'implementation to inherit.', 'True')
#     q.insert('Inheritance', 'In order to extend a class, the new class should have access to all the data and inner '
#                             'workings of the parent class.', 'False')
#     q.insert('Inheritance', 'An object-oriented program like Python supports not only inheritance but multiple '
#                             'inheritance as well.', 'True')
#     q.insert('Inheritance', 'Inheritance increases execution speed.', 'False')
#     q.insert('Polymorphism', 'Polymorphism enables objects of different classes that are related by a class hierarchy '
#                              'to be processed generically.', 'True')
#     q.insert('Polymorphism', 'The major drawback to polymorphism designed programs is that they do not consider '
#                              'the future addition or deletion of classes.', 'False')
#     q.insert('Polymorphism', 'Unfortunately, polymorphic programs make it difficult to add new capabilities to a '
#                              'system.', 'False')
#     q.insert('Polymorphism', 'Polymorphism is particularly effective for implementing layered software systems.', 'True')
#     q.insert('Polymorphism', 'Casting superclass references to subclass references is known as downcasting.', 'True')
