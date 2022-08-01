import unittest
import random
from phoenix_test import Phoenix
from warrior import Warrior
from mock_game import MockGame as Game


class Phoenix_Test(unittest.TestCase):
    def test_init(self):
        my_phoenix = Phoenix("Phoebe", Game())

    def test_name(self):
        my_phoenix = Phoenix("Phoebe", Game())
        self.assertEqual(my_phoenix.get_name(), "Phoebe")

    def test_str_(self):
        my_phoenix = Phoenix("Phoebe", Game())
        self.assertEqual(str(my_phoenix), "Phoebe")

    def test_name_fail(self):
        my_phoenix_fail = Phoenix("Phoebee", Game())
        self.assertNotEqual(my_phoenix_fail.get_name(), "Phoebe")
        self.assertNotEqual(str(my_phoenix_fail), "Phoebe")

    def test_Take_Damage(self):
        my_phoenix = Phoenix("Phoebe", Game())
        curr_hp = my_phoenix.__hp  # TODO change __hp to get_hp()
        self.assertEqual(my_phoenix.take_damage(5, source="unit tests"), None)
        self.assertEqual(Phoenix.__hp, 70)  # TODO change __hp to get_hp()

    def test_Deal_Damage(self):
        my_phoenix = Phoenix("Phoebe", Game())
        my_warrior = Warrior("Jack", Game())
        self.assertEqual(my_phoenix.deal_damage((5), source="unit tests"), None)
        self.assertEqual(my_warrior.__hp, 15)  # TODO change __hp to get_hp()

    def test_regenerate_hp(self):
        my_phoenix = Phoenix("Phoebe", Game())
        curr_hp = my_phoenix.__hp  # TODO change __hp to get_hp()
        self.assertEqual(my_phoenix.regenerate_hp(10), None)
        self.assertEqual(my_phoenix.__hp, curr_hp + 10)  # TODO change __hp to get_hp()

    def test_Chance_To_Dodge(self):
        my_phoenix = Phoenix("Phoebe", Game())
        self.assertEqual(my_phoenix.chance_to_dodge(random.uniform(.10, .20), source="unit tests"), None)
        # TODO determine proper chance to dodge

    def test_change_to_regenerate(self):
        my_phoenix = Phoenix("Phoebe", Game())
        self.assertEqual(my_phoenix.chance_to_regenerate(random.uniform(.10, .20), source="unit tests"), None)
        # TODO determine proper chance to regenerate

    def test_Attack_Speed(self):
        my_phoenix = Phoenix("Phoebe", Game())
        self.assertEqual(my_phoenix.attack_speed(4, source="unit tests"), None)


    def test_Chance_To_Hit(self):
        my_phoenix = Phoenix("Phoebe", Game())
        self.assertEqual(my_phoenix.chance_to_hit(random.randrange(1, 20), source="unit tests"), None)


if __name__ == '__main__':
    unittest.main()