#from replit import clear
import os
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
more_bidders = True
bidders = {}

while more_bidders:
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    bidders[name] = bid
    more = input("Are there other bidders? ")
    if more == "no":
        more_bidders = False
    else:
        os.system('cls')

# this is the cheat way
# max_bid = max(bidders, key=bidders.get)
# print(f"The winner is {max_bid} with a bid of ${bidders[max_bid]}")

# this is the way that I thought would not be suitable, but was
def find_highest_bidder(bidders):
    highest_bid = 0
    winner = ""
    for bidder in bidders:
        bid = bidders[bidder]
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
find_highest_bidder(bidders)