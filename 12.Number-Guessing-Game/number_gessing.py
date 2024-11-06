#import random
from random import randint 

# Opening message to user
print('Welcome to the Guessing Game')
print('Guess a number between 1 and 100')

#Choose a number b/t 1 - 100
answer = randint(1, 100)


# Function to set difficulty
def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer: 
        print("Your guess is too high, guess lower")
    elif user_guess < actual_answer:
        print("Too low, guess higher")
    else:
        print(f"You guessed it! The answer was {actual_answer}")


# Let user guess a number
guess = int(input("Make a guess: "))


# Check number against original number.


#Track number of guesses / turns


#repeat the guessing of they got it wrong