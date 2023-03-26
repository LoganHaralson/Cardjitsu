import random
import unittest


class Element:
    weaknesses = {
        'Fire': 'Water',
        'Snow': 'Fire',
        'Water': 'Snow'
    }

    def __init__(self, element):
        self.element = element

    def __lt__(self, other):
        return self.weaknesses[self.element] == other.element

    def __eq__(self, other):
        return self.element == other.element

    def __str__(self):
        return self.element


class Card:
    def __init__(self, color, rank, element):
        self.color = color
        self.rank = rank
        self.element = Element(element)

    def __str__(self):
        return f"{self.color} {self.rank} of {self.element}"

    def __lt__(self, other):
        if self.element < other.element:
            return True
        elif self.element == other.element:
            return self.rank < other.rank
        else:
            return False


class GameState:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()

    # for each round--
    def play_round(self):

        self.player1.draw_card()
        self.player2.draw_card()
        # determine which player is choosing a card to play

        # both players play a card
        card1 = self.player1.choose_card()
        card2 = self.player2.choose_card()
        print(f"{card1}, {card2}")
        # compare the cards and collect the winning card
        if card1 < card2:
            self.player2.collect_card(card2)
            print("Player 2 collected their card.")
        elif card2 < card1:
            self.player1.collect_card(card1)
            print("Player 1 collected their card.")
        else:
            print("No card was collected.")

        # determine a winning player based on collected cards
        # a player wins by collecting three cards of different colors with the same element or all three elements


class Player:
    def __init__(self):
        self.name = input("Enter your nickname: ")
        self.deck = Deck()
        self.deck.shuffle()
        self.hand = self.deck.draw_hand()
        self.card_collection = []

    def draw_card(self):
        self.hand.append(self.deck.take_card())

    def choose_card(self):
        n = 0
        for card in self.hand:
            print(f"{n+1}, {card}")
            n += 1
        print(f"{self.name}'s turn.")
        print("What card would you like to play from your hand?")
        played_card = int(input("Input a number 1 through 5: ")) - 1
        return self.hand.pop(played_card)

    def collect_card(self, card):
        self.card_collection.append(card)


class Computer(Player):
    def choose_card(self):
        return self.hand.pop()


class Deck:
    colors = ['red', 'blue', 'orange', 'green', 'yellow', 'purple']
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    elements = ['Fire', 'Water', 'Snow']
    # creates a collection of cards

    def __init__(self):
        cards = []
        for color in self.colors:
            for rank in self.ranks:
                for element in self.elements:
                    card = Card(color, rank, element)
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
    def test_element_eq(self):
        fire = Element("Fire")
        water = Element("Water")
        snow = Element("Snow")
        self.assertTrue(fire == fire)
        self.assertTrue(water == water)
        self.assertTrue(snow == snow)
        self.assertFalse(snow == fire)
        self.assertFalse(fire == water)
        self.assertFalse(water == snow)

    def test_element_lt(self):
        fire = Element("Fire")
        water = Element("Water")
        snow = Element("Snow")
        self.assertTrue(fire < water)
        self.assertTrue(water < snow)
        self.assertTrue(snow < fire)
        self.assertFalse(snow < snow)
        self.assertFalse(fire < fire)
        self.assertFalse(water < water)
        self.assertFalse(fire < snow)
        self.assertFalse(water < fire)
        self.assertFalse(snow < water)

    def test_card_eq(self):
        card1 = Card('orange', 4, 'Fire')
        card2 = Card('purple', 7, 'Water')
        card3 = Card('blue', 5, 'Snow')
        self.assertTrue(card1 == card1)
        self.assertTrue(card2 == card2)
        self.assertTrue(card3 == card3)
        self.assertFalse(card1 == card2)
        self.assertFalse(card2 == card3)
        self.assertFalse(card3 == card1)

    def test_card_lt(self):
        card1 = Card('orange', 4, 'Fire')
        card2 = Card('purple', 7, 'Water')
        card3 = Card('blue', 5, 'Water')
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

        if a player collects three differently colored cards of either the same element or different elements they win.

        When a player wins, declare the victor, end the game and ask if they want to play again.
        '''
