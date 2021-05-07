############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal():
    """Return a random card"""
    card_choice = random.randint(0,12)
    return cards[card_choice]

def play():
    player_hand = []
    computer_hand = []
    print(logo)
    play_blackjack = True
    while play_blackjack:
        #Start of the game - deal 2 cards to player, 1 to computer
        player_hand.append(deal())
        player_hand.append(deal())
        computer_hand.append(deal())
        player_sum = sum(player_hand)
        print(f"Your cards: {player_hand}, current score: {player_sum}")
        print(f"Computer's first card: {computer_hand}")

        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            player_hand.append(deal())
            player_sum = sum(player_hand)
            print(f"Your cards: {player_hand}, current score: {player_sum}")
            print(f"Computer's first card: {computer_hand}")
        else:
            print("Done")

        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
            play()
        else:
            quit()

if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play()
else:
    quit()