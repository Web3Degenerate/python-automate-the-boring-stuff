#import random
from random import randint 

#global constant for game level
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# TURNS = 0
turns = 0

# Function to check user guess to randomly generated answer:
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining"""
    if user_guess > actual_answer: 
        print("Your guess is too high, guess lower")
        # global TURNS
        # TURNS -= 1
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low, guess higher")
        # TURNS -= 1
        return turns - 1
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


def game(): 
    # Opening message to user
    print('Welcome to the Guessing Game')
    print('Guess a number between 1 and 100')

    #Choose a number b/t 1 - 100
    answer = randint(1, 100)
    #For testing, print out the answer: 
    print(f"Psssst, the correct answer is {answer}")


    # Set difficulty
    turns = set_difficulty()

    guess = 0
    # Let user guess again
    while guess != answer: 
        
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let user guess a number
        guess = int(input("Make a guess: "))

        # Check number against original number.
        # check_answer(guess, answer)

        # Add turns to check_answer()
        # check_answer(guess, answer, turns)

        # set check_answer to variable turns since check_answer returns udpated turns number
        # Run the code through pythonTutor.com/visualize.html#mode=edit
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, you lose!")
            # Use the return keyword to kick out of the function
            return 
        elif guess != answer:
            print('Guess again.')

    #Track number of guesses / turns

game()

#repeat the guessing of they got it wrong