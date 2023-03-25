import random

# Define the choices and ranks
elements = ['Fire', 'Water', 'Snow']
ranks = ['1', '2', '3', '4', '5', '6']
# Define which choices win against the other
strengths = {
    'Fire': 'Snow',
    'Snow': 'Water',
    'Water': 'Fire'
}

weaknesses = {
    'Fire': 'Water',
    'Snow': 'Fire',
    'Water': 'Snow'
}

# Define wins
player_wins = 0
computer_wins = 0

# Create a deck using the choices above
original_deck = [(rank, element) for rank in ranks for element in elements]

# Copy the deck for use in game
deck = original_deck.copy()

# Draw a hand of three cards for the player
hand = random.sample(deck, 3)

# Draw a hidden hand of three cards for the computer
hidden_hand = random.sample(deck, 3)

# Define compare cards function


def compare_cards(player_card, computer_card):
    global player_wins
    global computer_wins
    if player_card:
        if strengths[player_card[1]] == computer_card[1]:
            print('You won this round')
            player_wins += 1
            print('{} : {}'.format(player_wins, computer_wins))
        elif weaknesses[player_card[1]] == computer_card[1]:
            print('The computer won this round')
            computer_wins += 1
            print('{} : {}'.format(player_wins, computer_wins))
        else:
            if player_card[0] > computer_card[0]:
                print('You won this round.')
                player_wins += 1
                print('{} : {}'.format(player_wins, computer_wins))
            elif player_card[0] < computer_card[0]:
                print('The computer won this round')
                computer_wins += 1
                print('{} : {}'.format(player_wins, computer_wins))
            else:
                print("This shouldn't be possible")


while True:
    # print the player's hand
    if len(hand) > 0:
        print('your hand')
        for i, card in enumerate(hand):
            print('[{}]:{} of {}'.format(i+1, card[0], card[1]))

        # Prompt the user to play a choice
        while True:

            # Determine if there are any cards in hand
            if len(hand) > 0:
                player_choice = input(
                    'Awaiting input. Please select an option from above: ')
                if player_choice.isdigit() and 1 <= int(player_choice) <= len(hand):
                    break
                elif player_choice.isdigit() and int(player_choice) > len(hand):
                    print('Invalid input. Please try again.')

        # Play the selected card and remove it from your hand and the deck
        if len(hand) == 0:
            break
        index = int(player_choice) - 1
        player_choice, player_rank = hand.pop(index)
        player_card = (player_choice, player_rank)
        print('You played the {} of {}.'.format(player_choice, player_rank))

        # Play a random card from the hidden hand
        computer_choice, computer_rank = random.choice(hidden_hand)
        computer_card = (computer_choice, computer_rank)
        hidden_hand.remove(computer_card)
        print('The computer played the {} of {}'.format(
            computer_choice, computer_rank))

        # Determine and print the winner of the round
        compare_cards(player_card, computer_card)

        # Draw a new card to each hand
        if len(deck) > 0:
            hand.append(deck.pop())
            hidden_hand.append(deck.pop())
        else:
            print('There are no cards left to draw')
            if len(hand) == 0:
                if player_wins > computer_wins:
                    print('You won this match')
                elif computer_wins > player_wins:
                    print('The computer won this match')
                else:
                    print('This match ended in a draw')
                break
