#from replit import clear
import os
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
more_bidders = True
bidders = {}

while more_bidders:
    name = input("What is your name? ")
    bid = input("What's your bid? $")
    bidders[name] = bid
    more = input("Are there other bidders? ")
    if more == "no":
        more_bidders = False
    else:
        os.system('cls')

max_bid = max(bidders, key=bidders.get)
print(f"The winner is {max_bid} with a bid of ${bidders[max_bid]}")