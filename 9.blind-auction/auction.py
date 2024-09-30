import art
print(art.logo)

# TODO-1: Ask the user for input
# name = input('What is your name?: \n')
# price = int(input('What is your bid?: \n$'))

# bids dictionary
# bids = {}

# TODO-2: Save data into dictionary {name: price}
# bids[name] = price

# TODO-3: Whether if new bids need to be added
# should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")



# separate function
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f'The winner is {winner} with a bid of ${highest_bid}.')


# bids dictionary
bids = {}

continue_bidding = True
while continue_bidding:
    name = input('What is your name?: \n')
    price = int(input('What is your bid?: \n$'))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
# TODO-4: Compare bids in dictionary
    if should_continue == 'no':
        continue_bidding = False
        find_highest_bidder(bids)
    # elif should_continue == 'yes':
    else:
        # "Clear" the screen with 20 new lines
        print('\n' * 20)

#******* MAX FUNCTION: To use the max function: ******************************* #

# fruits = {'apple': 2, 'pear': 4, 'orange': 9}
# max(fruits, key=fruits.get)
# returns 'orange'