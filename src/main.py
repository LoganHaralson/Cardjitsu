import random
import unittest


class Weapon:
    weaknesses = {
        'Sword': 'Shield',
        'Bow': 'Sword',
        'Shield': 'Bow'
    }

    def __init__(self, weapon):
        self.weapon = weapon

    def __lt__(self, other):
        return self.weaknesses[self.weapon] == other.weapon

    def __eq__(self, other):
        return self.weapon == other.weapon

    def __str__(self):
        return self.weapon


class Card:
    def __init__(self, element, rank, weapon):
        self.element = element
        self.rank = rank
        self.weapon = Weapon(weapon)

    def __str__(self):
        return f"{self.element} {self.weapon} with power {self.rank}"

    def __lt__(self, other):
        if self.weapon < other.weapon:
            return True
        elif self.weapon == other.weapon:
            return self.rank < other.rank
        else:
            return False


class GameState:
    def __init__(self):
        print("Would you like to play against the computer or another player?")
        match_type = int(
            input("Enter 0 for computer match or 1 for a player match: "))

        self.player1 = Human()
        if match_type == 0:
            self.player2 = Computer()
        elif match_type == 1:
            self.player2 = Human()
        else:
            print("Error, invalid input. Please try again.")
            # for each round--

    def play_round(self):

        self.player1.draw_card()
        self.player2.draw_card()
        # determine which player is choosing a card to play

        # both players play a card
        card1 = self.player1.choose_card()
        card2 = self.player2.choose_card()
        print(f"{self.player1.name}'s card: {card1}")
        print(f"{self.player2.name}'s card: {card2}")
        # compare the cards and collect the winning card
        if card1 < card2:
            self.player2.collect_card(card2)
            print(f"{self.player2.name} collected their card.")
        elif card2 < card1:
            self.player1.collect_card(card1)
            print(f"{self.player1.name} collected their card.")
        else:
            print("No card was collected.")

        # determine a winning player based on collected cards
        # a player wins by collecting three cards of different elements with the same weapon or all three weapons


class Player:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.hand = self.deck.draw_hand()
        self.card_collection = []

    def draw_card(self):
        self.hand.append(self.deck.take_card())

    def choose_card(self):
        print("\n")
        print(f"{self.name}'s turn.")
        print("\n")
        n = 0
        for card in self.hand:
            print(f"{n+1}, {card}")
            n += 1
        print("\n")
        print("Which card would you like to play from your hand?")
        played_card = int(input("Input a number 1 through 5: ")) - 1
        print("\n")
        return self.hand.pop(played_card)

    def collect_card(self, card):
        self.card_collection.append(card)


class Human(Player):
    def __init__(self):
        self.name = input("Enter your nickname: ")
        super().__init__()


class Computer(Player):
    def __init__(self):
        self.name = "Computer"
        super().__init__()

    def choose_card(self):
        return self.hand.pop()
    # have the computer choose a random card here


class Deck:
    elements = ['Fire', 'Water', 'Void', 'Earth', 'Lightning', 'Crystal']
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    weapons = ['Sword', 'Shield', 'Bow']
    # creates a collection of cards

    def __init__(self):
        cards = []
        for element in self.elements:
            for rank in self.ranks:
                for weapon in self.weapons:
                    card = Card(element, rank, weapon)
                    cards.append(card)
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def take_card(self):
        return self.cards.pop(0)

    def draw_hand(self):
        hand = []
        for i in range(4):
            hand.append(self.take_card())
        return hand


class TestFunctions(unittest.TestCase):
    def test_weapon_eq(self):
        Sword = Weapon("Sword")
        Shield = Weapon("Shield")
        Bow = Weapon("Bow")
        self.assertTrue(Sword == Sword)
        self.assertTrue(Shield == Shield)
        self.assertTrue(Bow == Bow)
        self.assertFalse(Bow == Sword)
        self.assertFalse(Sword == Shield)
        self.assertFalse(Shield == Bow)

    def test_weapon_lt(self):
        Sword = Weapon("Sword")
        Shield = Weapon("Shield")
        Bow = Weapon("Bow")
        self.assertTrue(Sword < Shield)
        self.assertTrue(Shield < Bow)
        self.assertTrue(Bow < Sword)
        self.assertFalse(Bow < Bow)
        self.assertFalse(Sword < Sword)
        self.assertFalse(Shield < Shield)
        self.assertFalse(Sword < Bow)
        self.assertFalse(Shield < Sword)
        self.assertFalse(Bow < Shield)

    def test_card_eq(self):
        card1 = Card('void', 4, 'Sword')
        card2 = Card('Crystal', 7, 'Shield')
        card3 = Card('Water', 5, 'Bow')
        self.assertTrue(card1 == card1)
        self.assertTrue(card2 == card2)
        self.assertTrue(card3 == card3)
        self.assertFalse(card1 == card2)
        self.assertFalse(card2 == card3)
        self.assertFalse(card3 == card1)

    def test_card_lt(self):
        card1 = Card('void', 4, 'Sword')
        card2 = Card('Crystal', 7, 'Shield')
        card3 = Card('Water', 5, 'Shield')
        self.assertTrue(card1 < card2)
        self.assertTrue(card1 < card3)
        self.assertTrue(card3 < card2)
        self.assertFalse(card2 < card1)
        self.assertFalse(card2 < card3)
        self.assertFalse(card3 < card1)


if __name__ == "__main__":
    # unittest.main()
    gamestate = GameState()
    while 0 != 1:
        gamestate.play_round()
        ''' 
        find a way to get user input and pass it to the gamestate
        implement game logic: User input, how it effects each round, how a player wins and what happens when a player wins.
        
        
        
        print which player's turn it is
        print the player's hand
        get user input: determine played cards
        prompt: Which card would you like to play from your hand?
        Input a number 1 through 5. :

        after both players select their cards, compare the two cards and determine the winning card.

        the winning player collects the card that they played to a seperate deck while the losing player discards their's.

        if a player collects three of the same weapons with different elements or all three weapons of different elements, they win the game.
        
        When a player wins, declare the victor, end the game and ask if they want to play again.
        '''
