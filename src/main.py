import random


class Weapon:
    weaknesses = {
        'Shield': 'Sword',
        'Bow': 'Shield',
        'Sword': 'Bow'
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
        prompt = "Enter 0 for computer match or 1 for a player match: "
        self.player1 = Human()

        print("Would you like to play against the computer or another player?")
        while True:
            try:
                match_type = int(input(prompt))
            except Exception:
                print("Error! Invalid input.")
                continue
            if match_type == 0:
                self.player2 = Computer()
                return
            if match_type == 1:
                self.player2 = Human()
                return
            print("Invalid input, expected a 0 or a 1")

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


class OutOfRange(Exception):
    def __init__(self, entered):
        self.entered = entered
        super().__init__()

    def __str__(self):
        return f"You entered {self.entered}, expected 1 through 5"


class Player:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.hand = self.deck.draw_hand()
        self.card_collection = []

    def draw_card(self):
        self.hand.append(self.deck.take_card())

    def choose_card(self):
        print()
        print(f"{self.name}'s turn.")
        print()
        n = 0
        for card in self.hand:
            print(f"{n+1}, {card}")
            n += 1
        print()
        print("Which card would you like to play from your hand?")
        while True:
            try:
                played_card = int(input("Input a number 1 through 5: "))
                if played_card < 1 or played_card > 5:
                    raise OutOfRange(played_card)
            except ValueError as err:
                print("Invalid input. Expected a number")
            except OutOfRange as err:
                print(err)
            else:
                return self.hand.pop(played_card - 1)

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
        # the computer randomly selects a card from it's hand
        index = random.randint(0, 4)
        return self.hand.pop(index)


class Deck:
    elements = ['Fire', 'Water', 'Void', 'Earth', 'Lightning', 'Crystal']
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    weapons = ['Shield', 'Sword', 'Bow']
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


# This class will keep track of the collected cards and look for win conditions
class winGame:
    def __init__(self):
        pass


if __name__ == "__main__":
    # unittest.main()
    gamestate = GameState()
    while 0 != 1:
        gamestate.play_round()
        ''' 

        if a player collects three of the same weapons with different elements or all three weapons of different elements, they win the game.
        
        When a player wins, declare the victor, end the game and ask if they want to play again.
        '''
