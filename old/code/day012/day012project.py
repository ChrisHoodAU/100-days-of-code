# Easy: 10 attempts
# Hard: 5 attempts
import random
difficulty = {
    "easy": 10,
    "hard": 5
}
# select starting number
CHOSEN_NUMBER = random.randint(1,100)

# check guess function
def check_guess(computer, user):
    if user == computer:
        return f"You got it! The answer was {computer}"
    if user < computer:
        return "Too low, guess again"
    if user > computer:
        return "Too high, guess again"

# check if guesses remain
def check_remaining(guesses):
    if guesses > 0:
        return True
    else:
        return False

def make_a_guess(number_of_guesses):
    print(f"You have {number_of_guesses} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    number_of_guesses -= 1
    if guess != CHOSEN_NUMBER:
        print(check_guess(CHOSEN_NUMBER, guess))
        if check_remaining(number_of_guesses):
            make_a_guess(number_of_guesses)
        else:
            print("You have run out of guesses. You Lose.")
    else:
        print(check_guess(CHOSEN_NUMBER, guess))

#helpful for testing
#print(CHOSEN_NUMBER)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
number_of_guesses = difficulty[input("Choose a difficulty. Type 'easy' or 'hard': ")]
make_a_guess(number_of_guesses)