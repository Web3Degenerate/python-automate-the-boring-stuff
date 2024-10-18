import random

def deal_card():
    """Returns a random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []

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

def calculate_score(cards):
    sum(cards)