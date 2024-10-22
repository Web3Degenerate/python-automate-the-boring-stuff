import random

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


user_cards = []
computer_cards = []
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