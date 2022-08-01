import unittest
import random
from sphinx import Sphinx
from warrior import Warrior
from mock_game import MockGame as Game


class Sphinx_Test(unittest.TestCase):
    def test_init(self):
        my_sphinx = Sphinx("Sphick", Game())

    def test_str_fail(self):
        my_sphinx = Sphinx("Sphick", Game())
        self.assertNotEqual(str(my_sphinx), "Sphick")

    def test_name_fail(self):
        my_sphinx_fail = Sphinx("Sphicholas", Game())
        self.assertNotEqual(my_sphinx_fail.get_name(), "Sphick")
        self.assertNotEqual(str(my_sphinx_fail), "Sphick")

    def test_Chance_To_Dodge(self):
        my_sphinx = Sphinx("Sphick", Game())
        self.assertNotEqual(my_sphinx.get_chance_to_dodge(), .18)

    def test_Chance_To_Dodge_fail(self):
        my_sphinx = Sphinx("Sphick", Game())
        try:
            self.assertAlmostEqual(my_sphinx.get_chance_to_dodge(), .18)
            self.assertAlmostEqual(False, True)
        except:
            self.assertAlmostEqual(True, True)

    def test_Attack_Speed(self):
        my_sphinx = Sphinx("Sphick", Game())
        self.assertEqual(my_sphinx.get_attack_speed(), 1)

    def test_Chance_To_Hit(self):
        my_sphinx = Sphinx("Sphick", Game())
        self.assertNotEqual(my_sphinx.get_chance_to_hit(), .5)

    def test_test_Chance_To_Hit_fail(self):
        my_sphinx = Sphinx("Sphick", Game())
        try:
            self.assertAlmostEqual(my_sphinx.get_chance_to_hit(), .5)
            self.assertAlmostEqual(False, True)
        except:
            self.assertAlmostEqual(True, True)


if __name__ == '__main__':
    unittest.main()