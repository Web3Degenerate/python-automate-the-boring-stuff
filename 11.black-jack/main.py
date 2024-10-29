import random
# to import the ascii art: 
# from art import logo

def deal_card():
    """Returns a random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards"""
    """ Check for 11, 10 and length of 2, ie blackjack with 2 cards"""
    # if 11 in cards and 10 in cards and len(cards) == 2:
    """ refactor """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    """ Check for changing 11 to 1 """
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


#TODO 13
def compare(u_score, c_score):
    if u_score == c_score: 
        return "Draw "
    elif c_score == 0:
       return "lose, Dealer has Blackjack" 
    elif u_score == 0:
        return "Win, with a blackjack"
    elif u_score >21:
        return "You busted out"
    elif c_score >21:
        return "Dealer busted! You win"
    elif u_score > c_score:
        return "You win this hand!"
    else:
        return "Dealer wins...again."

#Finally, wrap our game code in it's own function for the final while loop (game continuation) at the bottom. 
def play_game():
    #to import ASCII art at start of game: print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1 #to prevent computer_score from being undefined
    user_score = -1 #to prevent user_score from being undefined. 
    is_game_over = False

    """If you don't need a variable you can use an underscore _ """
    for _ in range(2):
        """ NOTE: += is the same thing as .extend() which expects a list
        user_cards += new_card 
        user_cards.extend(new_card)
        Returns TYPE ERROR: `int object not iterable`
        
        To fix you could do
        new_card = [deal_card()]  => call the function into a list
        user_card += new_card
        """
        """Returns a random card from the deck"""
        # new_card = deal_card()
        # user_cards.append(new_card)
        """refactor: """
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over: 
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are {user_cards} and your score is {user_score}")
        print(f"Dealer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score >21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card. Type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # (12). Computer should draw if less than 17, but stop when 21 or over
    while computer_score != 0 and computer_score <17:
        computer_cards.append(deal_card())
        """computer_score is defined in while loop above. If no value, undefined"""
        computer_score = calculate_score(computer_cards)


    #Final comparing of user vs dealer score: 
    print(f"Your final hand {user_cards}, Your hand total: {user_score}")
    print(f"Dealer final hand {computer_cards}, Dealer hand total: {computer_score}")
    print(compare(user_score, computer_score))


# prompt the user to play another hand: 
while input("Do you want to play another hand? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()