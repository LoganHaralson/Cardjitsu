import unittest
from main import *


class TestFunctions(unittest.TestCase):
    def test_weapon_eq(self):
        Shield = Weapon("Shield")
        Sword = Weapon("Sword")
        Bow = Weapon("Bow")
        self.assertTrue(Shield == Shield)
        self.assertTrue(Sword == Sword)
        self.assertTrue(Bow == Bow)
        self.assertFalse(Bow == Shield)
        self.assertFalse(Shield == Sword)
        self.assertFalse(Sword == Bow)

    def test_weapon_lt(self):
        Shield = Weapon("Shield")
        Sword = Weapon("Sword")
        Bow = Weapon("Bow")
        self.assertTrue(Shield < Sword)
        self.assertTrue(Sword < Bow)
        self.assertTrue(Bow < Shield)
        self.assertFalse(Bow < Bow)
        self.assertFalse(Shield < Shield)
        self.assertFalse(Sword < Sword)
        self.assertFalse(Shield < Bow)
        self.assertFalse(Sword < Shield)
        self.assertFalse(Bow < Sword)

    def test_card_eq(self):
        card1 = Card('void', 4, 'Shield')
        card2 = Card('Crystal', 7, 'Sword')
        card3 = Card('Water', 5, 'Bow')
        self.assertTrue(card1 == card1)
        self.assertTrue(card2 == card2)
        self.assertTrue(card3 == card3)
        self.assertFalse(card1 == card2)
        self.assertFalse(card2 == card3)
        self.assertFalse(card3 == card1)

    def test_card_lt(self):
        card1 = Card('void', 4, 'Shield')
        card2 = Card('Crystal', 7, 'Sword')
        card3 = Card('Water', 5, 'Sword')
        self.assertTrue(card1 < card2)
        self.assertTrue(card1 < card3)
        self.assertTrue(card3 < card2)
        self.assertFalse(card2 < card1)
        self.assertFalse(card2 < card3)
        self.assertFalse(card3 < card1)


if __name__ == "__main__":
    unittest.main()
