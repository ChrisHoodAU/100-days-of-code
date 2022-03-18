# import random
import random
# import logos
from art import logo
from art import vs
# import data
from game_data import data
import os

# get the length of the list
NUM_OF_FACTS = len(data)
NAME = 'name'
FOLLOWER_COUNT = 'follower_count'
DESCRIPTION = 'description'
COUNTRY = 'country'

# get a random list item
def get_fact(data, number):
    # print(data[number]['name'])
    # print(data[number]['follower_count'])
    # print(data[number]['description'])
    # print(data[number]['country'])
    return data[number]

def check_answer(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == "a" # this is instead of a second if statement, if guess == a return true
    else:
        return guess == "b"

def play(score, a_item, a_num):
    # get a second random list item
    win_streak = True
    
    while win_streak:
        b_num = random.randint(0,NUM_OF_FACTS - 1) # random.choice(data)
        # ensure they are not the same item
        while a_num == b_num:
            b_num = random.randint(0,NUM_OF_FACTS - 1) # random.choice(data)
        b_item = get_fact(data, b_num)

        # print(a_item)
        # print(b_item)
        # print(item[NAME])
        # print(item[FOLLOWER_COUNT])
        # print(item[DESCRIPTION])
        # print(item[COUNTRY])

        # Higher Lower Logo
        os.system('cls')
        print(logo)
        if score != 0:
            print(f"You're right! Current score: {score}")
        # Compare A: <name>, a <job>, from <location>
        print(f"Compare A: {a_item[NAME]}, a {a_item[DESCRIPTION]}, from {a_item[COUNTRY]}")
        # logo vs
        print(vs)
        # Against B: <name>, a <job>, from <location>
        print(f"Against B: {b_item[NAME]}, a {b_item[DESCRIPTION]}, from {b_item[COUNTRY]}")
        # If right, swap B to A, generate a new B
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = check_answer(answer, a_item[FOLLOWER_COUNT], b_item[FOLLOWER_COUNT])
        # if answer == 'a':
        #     guess = a_item[FOLLOWER_COUNT]
        #     other = b_item[FOLLOWER_COUNT]
        # else:
        #     guess = b_item[FOLLOWER_COUNT]
        #     other = a_item[FOLLOWER_COUNT]
        if is_correct:
            a_item = b_item
            a_num = b_num
            score += 1
            play(score, b_item, b_num)
            os.system('cls')
        else:
            os.system('cls')
            print(f"Sorry, that's wrong. Final score: {score}")
            win_streak = False
            quit()
        # If wrong, exit with score

score = 0
a_num = random.randint(0,NUM_OF_FACTS - 1)
a_item = get_fact(data, a_num)
play(score, a_item, a_num)

#either a while loop with a condition or a recurse. not both.