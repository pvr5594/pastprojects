import unittest
from quiz import Quiz
from sqliteselect import Select


class QuizTest(unittest.TestCase):

    def test_create(self):
        """
        Test if a database file is created
        """
        quiz = Quiz()
        quiz.create()

    def test_insert(self):
        """
        Test if data can be inserted into database
        """
        quiz = Quiz()
        sqlite_select = Select()
        database = r"dungeonquiz.db"
        conn = sqlite_select.create_connection(database)
        quiz.insert('Test', 'Test Question', 'Test Answer')
        cur = conn.cursor()
        category = 'Test'
        cur.execute("SELECT * FROM quiz WHERE category=?", (category,))
        rows = cur.fetchone()
        sqlite_select.selected_quiz(rows)

        tq = 'Test Question'
        ta = 'Test Answer'

        self.assertEqual(rows[2], tq)
        self.assertEqual(rows[3], ta)

    def test_update_fail(self):
        """
        Test if a selected question successfully updates
        """
        quiz = Quiz()
        quiz.update('21', 'Category', 'Question', 'Answer')
        sqlite_select = Select()
        database = r"dungeonquiz.db"
        conn = sqlite_select.create_connection(database)

        q_id = '21'
        rows = sqlite_select.selected_quiz(sqlite_select.select_quiz_by_priority(conn, q_id))

        tc = 'Category'
        tq = 'Question'
        ta = 'Answer'

        self.assertNotEqual(rows[1], tc)
        self.assertNotEqual(rows[2], tq)
        self.assertNotEqual(rows[3], ta)

        quiz.update('21', 'Test', 'Test Question', 'Test Answer')

    def test_select(self):
        """
        Test if data can be selected specifically
        """
        quiz = Quiz()
        tca = 'Abstraction'
        tce = 'Encapsulation'
        tci = 'Inheritance'
        tcp = 'Polymorphism'

        rows = quiz.select('Abstraction')
        self.assertEqual(rows[1], tca)

        rows = quiz.select('Encapsulation')
        self.assertEqual(rows[1], tce)

        rows = quiz.select('Inheritance')
        self.assertEqual(rows[1], tci)

        rows = quiz.select('Polymorphism')
        self.assertEqual(rows[1], tcp)


if __name__ == '__main__':
    unittest.main()
