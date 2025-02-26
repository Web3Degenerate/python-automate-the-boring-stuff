
# Display Art
from highlowart import logo, vs
print(logo)

# Generate a random account from game_data.py
import random 

# Import game_data
from game_data import data



def format_data(account):
    """ Format the account data into printable format"""
    account_name = account_a["name"]
    account_descr = account_a["description"]
    account_country = account_a["country"]
    # print(f"{account_name}, a {account_descr}, from {account_country}")
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """ Take the user's guess and the follower counts and returns if the user got it right"""
    #cumbersome way, 4 if statements
        # if a_followers > b_followers and user_guess == "a":
    # Instead use nested if statements
    if a_followers > b_followers: 
        # if user_guess == "a":
        #     return True
        # else: 
        #     return False
        #ABOVE CODE is the same as just saying return user_guess = "a". Evaluautes to true/false the same way
        return user_guess == "a"
    else: 
        return user_guess == "b"


score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    # Making account at position B become the next account position A
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        #set account b to a random selection from our data set
        account_b = random.choice(data)


    print(f"Comare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess
    guess = input("Who has more followers, Type 'A' or 'B': ").lower()

    #Clear the screen
    print("\n *20")
    print(logo)

    ## - Get Follower count for each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]


    # Check if user is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count) #true or false

    # Give user feedback on their guess
    # Score keeping

    if is_correct: 
        score += 1
        print(f"You're right. Current score {score}")
    else: 
        print(f"Sorry, that's wrong. Your Final Score: {score}")
        game_should_continue = False





