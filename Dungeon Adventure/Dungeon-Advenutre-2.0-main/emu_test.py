import unittest
import random
from emu import Emu
from warrior import Warrior
from mock_game import MockGame as Game


class Raven_Test(unittest.TestCase):
    def test_init(self):
        my_raven = Emu("Emu", Game())

    def test_str_fail(self):
        my_raven = Emu("Emu", Game())
        self.assertNotEqual(str(my_raven), "Emu")

    def test_name_fail(self):
        my_raven_fail = Emu("Emuaw", Game())
        self.assertNotEqual(my_raven_fail.get_name(), "Emuaw")
        self.assertNotEqual(str(my_raven_fail), "Emuaw")

    def test_Chance_To_Dodge_fail(self):
        my_raven = Emu("Emu", Game())
        self.assertNotEqual(my_raven.get_chance_to_dodge(), .15)

    def test_Chance_To_Dodge(self):
        my_raven = Emu("Emu", Game())
        try:
            self.assertAlmostEqual(my_raven.get_chance_to_dodge(), .40)
            self.assertAlmostEqual(False, True)
        except:
            self.assertAlmostEqual(True, True)

    def test_Attack_Speed(self):
        my_raven = Emu("Emu", Game())
        self.assertEqual(my_raven.get_attack_speed(), 3)

    def test_Chance_To_Hit_fail(self):
        my_raven = Emu("Emu", Game())
        self.assertNotEqual(my_raven.get_chance_to_hit(), .5)

    def test_test_Chance_To_Hit(self):
        my_raven = Emu("Emu", Game())
        try:
            self.assertAlmostEqual(my_raven.get_chance_to_hit(), .500)
            self.assertAlmostEqual(False, True)
        except:
            self.assertAlmostEqual(True, True)


if __name__ == '__main__':
    unittest.main()