MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients): 
    """Returns True when order can be made, False if ingredients are insufficient"""
    # Takes dictionary sepcified {'ingredients': {'water': 200, 'milk': 150, 'coffee': 24}, 'cost': 2.5}
    # is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]: # water:200 not >= water: 300
            print(f"Sorry, there is not enough {item}.")
            return False #return is_enough = False
    return True  # return is_enough

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """ Returns True when payment is acccepted, or False if money insufficent"""
    if money_received >= drink_cost:
        #calculate user's change
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change ${change}")
        #reach our global scope profit variable above with keyword 'global'
        global profit
        profit += drink_cost 
        return True
    else: 
        print("Sorry, that's not enough money. Money refunded")
        return False 


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    #loop through the ingredients
    for item in order_ingredients: 
        #subtract the order ingredients
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")

is_on = True

while is_on: 
    choice = input("What would you like (espresso/latte/cappuccino):" )
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else: 
        drink = MENU[choice]
        print(drink)
        if is_resource_sufficient(drink["ingredients"]): # MENU[choice]["ingredients"]
            # print("ok")
            payment = process_coins() #capture user's payment

            #call our transaction check function - IF payment is successful
            if is_transaction_successful(payment, drink["cost"]): # Menu["espresso"]["cost"]
                #pass in drink_name, order_ingredients
                make_coffee(choice, drink["ingredients"])
