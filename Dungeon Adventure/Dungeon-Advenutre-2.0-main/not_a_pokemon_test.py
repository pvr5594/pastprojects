import unittest
import random
from not_a_pokemon import not_a_Pokemon
from warrior import Warrior
from mock_game import MockGame as Game


class not_a_Pokemon_Test(unittest.TestCase):
    def test_init(self):
        my_not_a_pokemon = not_a_Pokemon("Pika", Game())

    def test_name(self):
        my_not_a_pokemon = not_a_Pokemon("Pika", Game())
        self.assertEqual(my_not_a_pokemon.get_name(), "Pika")

    def test_str_(self):
        my_not_a_pokemon = not_a_Pokemon("Pika", Game())
        self.assertEqual(str(my_not_a_pokemon), "Pika")

    def test_name_fail(self):
        my_not_a_pokemon_fail = not_a_Pokemon("Pikachu", Game())
        self.assertNotEqual(my_not_a_pokemon_fail.get_name(), "Pika")
        self.assertNotEqual(str(my_not_a_pokemon_fail), "Pika")

    def test_Take_Damage(self):
        my_not_a_pokemon = not_a_Pokemon("Pika", Game())
        curr_hp = my_not_a_pokemon.__hp  # TODO change __hp to get_hp()
        self.assertEqual(my_not_a_pokemon.take_damage(5, source="unit tests"), None)
        self.assertEqual(not_a_Pokemon.__hp, 70)  # TODO change __hp to get_hp()

    def test_Deal_Damage(self):
        my_not_a_pokemon = not_a_Pokemon("Pika", Game())
        my_warrior = Warrior("Jack", Game())
        self.assertEqual(my_not_a_pokemon.deal_damage(5, source="unit tests"), None)
        self.assertEqual(my_warrior.__hp, 15)  # TODO change __hp to get_hp()

    def test_regenerate_hp(self):
        my_not_a_pokemon = not_a_Pokemon("Pika", Game())
        curr_hp = my_not_a_pokemon.__hp  # TODO change __hp to get_hp()
        self.assertEqual(my_not_a_pokemon.regenerate_hp(10), None)
        self.assertEqual(my_not_a_pokemon.__hp, curr_hp + 10)  # TODO change __hp to get_hp()

    def test_Chance_To_Dodge(self):
        my_not_a_pokemon = not_a_Pokemon("Pika", Game())
        self.assertEqual(my_not_a_pokemon.chance_to_dodge(random.uniform(.10, .20), source="unit tests"), None)
        # TODO determine proper chance to dodge

    def test_change_to_regenerate(self):
        my_not_a_pokemon = not_a_Pokemon("Pika", Game())
        self.assertEqual(my_not_a_pokemon.chance_to_regenerate(random.uniform(.10, .20), source="unit tests"), None)
        # TODO determine proper chance to regenerate

    def test_Attack_Speed(self):
        my_not_a_pokemon = not_a_Pokemon("Pika", Game())
        self.assertEqual(my_not_a_pokemon.attack_speed(4, source="unit tests"), None)


    def test_Chance_To_Hit(self):
        my_not_a_pokemon = not_a_Pokemon("Pika", Game())
        self.assertEqual(my_not_a_pokemon.chance_to_hit(random.randrange(1, 20), source="unit tests"), None)


if __name__ == '__main__':
    unittest.main()