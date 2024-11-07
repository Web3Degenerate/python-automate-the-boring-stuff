#import random
from random import randint 

#global constant for game level
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Opening message to user
print('Welcome to the Guessing Game')
print('Guess a number between 1 and 100')

#Choose a number b/t 1 - 100
answer = randint(1, 100)
#For testing, print out the answer: 
print(f"Psssst, the correct answer is {answer}")

# Function to check user guess to randomly generated answer:
def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer: 
        print("Your guess is too high, guess lower")
    elif user_guess < actual_answer:
        print("Too low, guess higher")
    else:
        print(f"You guessed it! The answer was {actual_answer}")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty, Type 'easy' or 'hard': ")
    #Without the return statments below, we'd have to use "global turns"
    if level == 'easy':
        # turns = EASY_LEVEL_TURNS
        return EASY_LEVEL_TURNS
    else: 
        # turns = HARD_LEVEL_TURNS
        return HARD_LEVEL_TURNS

# Set difficulty
turns = set_difficulty()
print(f"You have {turns} attempts remaining to guess the number.")

# Let user guess a number
guess = int(input("Make a guess: "))

# Check number against original number.
check_answer(guess, answer)

#Track number of guesses / turns


#repeat the guessing of they got it wrong