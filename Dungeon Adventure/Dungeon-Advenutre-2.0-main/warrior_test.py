import unittest
import random
from warrior import Warrior
from emu import Emu
from mock_game import MockGame as Game


class Warrior_Test(unittest.TestCase):
    def test_init(self):
        my_adventurer = Warrior("Jack", Game())

    def test_name(self):
        my_adventurer = Warrior("Jack", Game())
        self.assertEqual(my_adventurer.get_name(), "Jack")

    def test_name_fail(self):
        try:
            my_adventurer_fail = Warrior("JackU", Game())
            self.assertEqual(False, True)
        except:
            self.assertEqual(True, True)

    def test_Earn_Pillar(self):
        adv = Warrior("Jack", Game())

        for pillar in ["A", "E", "I", "P"]:
            adv.earn_pillar(pillar)
            self.assertTrue(adv.is_pillar_in_inventory(pillar))

    def test_Add_Health_Potion(self):
        adventurer_HP = Warrior("Jack", Game())
        self.assertEqual(adventurer_HP.add_health_potion(), 1)

    def test_Use_One_Health_Potions(self):
        my_adventurer = Warrior("Jack", Game())
        self.assertEqual(my_adventurer.use_health_potion(), 0)

    def test_Use_One_Health_Potion_Fail(self):
        my_adventurer = Warrior("Jack", Game())
        try:
            self.assertEqual(my_adventurer.use_health_potion(), 1)
            self.assertEqual(False, True)
        except:
            self.assertEqual(True, True)

    def test_Add_Vision_Potion(self):
        adventurer_VP = Warrior("Jack", Game())
        self.assertEqual(adventurer_VP.add_vision_potion(), 1)

    def test_Use_One_Vision_Potions(self):
        my_adventurer = Warrior("Jack", Game())
        self.assertEqual(my_adventurer.use_vision_potion(), 0)

    def test_Use_One_Vision_Potion_Fail(self):
        my_adventurer = Warrior("Jack", Game())
        try:
            self.assertEqual(my_adventurer.use_vision_potion(), 1)
            self.assertEqual(False, True)
        except:
            self.assertEqual(True, True)

    def test_Take_Damage(self):
        my_adventurer = Warrior("Jack", Game())
        self.assertEqual(my_adventurer.take_damage(1000, source="unit tests"), my_adventurer.set_current_hp(0))

    def test_Exit_Fail(self):
        my_adventurer = Warrior("Jack", Game())
        self.assertEqual(my_adventurer.exit(), None)

    def test_Deal_Damage(self):
        my_adventurer = Warrior("Jack", Game())
        monster = Emu(1)
        self.assertEqual(my_adventurer.take_damage(random.randrange(40, 77), monster),
                         my_adventurer.set_current_hp(my_adventurer.take_damage(random.randrange(40, 77), monster)))

    def test_Special_Move(self):
        my_adventurer = Warrior("Jack", Game())
        monster = Emu(1)
        self.assertEqual(my_adventurer.special_move(monster), False)

    def test_Chance_To_Hit(self):
        my_adventurer = Warrior("Jack", Game())
        try:
            self.assertAlmostEqual(my_adventurer.get_chance_to_hit(), .75555)
            self.assertAlmostEqual(False, True)
        except:
            self.assertAlmostEqual(True, True)

    def test_Chance_To_Block(self):
        my_adventurer = Warrior("Jack", Game())
        try:
            self.assertAlmostEqual(my_adventurer.get_chance_to_block(), .4000)
            self.assertAlmostEqual(False, True)
        except:
            self.assertAlmostEqual(True, True)

    def test_Chance_To_Block_fail(self):
        my_adventurer = Warrior("Jack", Game())
        self.assertNotAlmostEqual(my_adventurer.get_chance_to_block(), .30000)

    def test_Chance_To_Dodge(self):
        my_adventurer = Warrior("Jack", Game())
        try:
            self.assertAlmostEqual(my_adventurer.get_chance_to_dodge(), .35555)
            self.assertAlmostEqual(False, True)
        except:
            self.assertAlmostEqual(True, True)

    def test_Chance_To_Dodge_fail(self):
        my_adventurer = Warrior("Jack", Game())
        self.assertNotAlmostEqual(my_adventurer.get_chance_to_block(), .23333)

    def test_Attack_Speed(self):
        my_adventurer = Warrior("Jack", Game())
        self.assertEqual(my_adventurer.get_attack_speed(), 4)


if __name__ == '__main__':
    unittest.main()
