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

def check_result(player_hand, computer_hand):
    player_sum = sum(player_hand)
    computer_sum = sum(computer_hand)
    print(f"    Your final hand: {player_hand}, final score: {player_sum}")
    print(f"    Computer's final hand: {computer_hand}, final score: {computer_sum}")
    if player_sum == 21 and len(player_hand) == 2:
        print("Blackjack! You Win!")
        return
    elif player_sum > 21:
        print("You went over. Computer wins.")
        return
    elif computer_sum > 21:
        print("Computer went over. You win.")
        return
    elif player_sum > computer_sum:
        print("You Win")
        return
    elif player_sum == computer_sum:
        print("Tie")
        return
    else:
        print("Computer wins.")
        return

def play():
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        player_hand = []
        computer_hand = []
        print(logo)
        another_card = True
        play_blackjack = True
        while play_blackjack:
            #Start of the game - deal 2 cards to player, 1 to computer
            player_hand.append(deal())
            player_hand.append(deal())
            computer_hand.append(deal())
            player_sum = sum(player_hand)
            computer_sum = sum(computer_hand)
            print(f"Your cards: {player_hand}, current score: {player_sum}")
            print(f"Computer's first card: {computer_hand}")

            while another_card == True:
                if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                    player_hand.append(deal())
                    player_sum = sum(player_hand)
                    print(f"    Your cards: {player_hand}, current score: {player_sum}")
                    print(f"    Computer's first card: {computer_hand}")
                    computer_sum = sum(computer_hand)
                    if player_sum == 21 and len(player_hand) == 2:
                        check_result(player_hand, computer_hand)
                        play()
                    elif player_sum > 21:
                        while computer_sum <=16:
                            computer_hand.append(deal())
                            computer_sum = sum(computer_hand)
                        check_result(player_hand, computer_hand)
                        play()
                else:
                    while computer_sum <=16:
                        computer_hand.append(deal())
                        computer_sum = sum(computer_hand)
                    check_result(player_hand, computer_hand)
                    another_card = False
                    play()
    else:
        play_blackjack = False
        quit()

# Main Body
play()