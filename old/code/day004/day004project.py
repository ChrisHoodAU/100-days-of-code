rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
options = [rock, paper, scissors]
print(options[int(user_choice)])

computer_choice = random.randint(0,2)
print(f"Computer chose:\n{options[computer_choice]}")

if (int(user_choice) == computer_choice):
    print("It's a Draw.")
elif (int(user_choice) == 2 and computer_choice == 0):
    print("You Lose.")
elif (int(user_choice) == 0 and computer_choice == 2):
    print("You Win!")
elif (int(user_choice) > computer_choice):
    print("You Win!")
elif (int(user_choice) < computer_choice):
    print("You Lose.")