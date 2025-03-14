from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()

coffee_maker = CoffeeMaker()

coffee_maker.report()
money_machine.report()

#resume at Sec 16, v.114 at (3:53)

# set up while loop to handle the condition when coffee machine is on
is_on = True
menu = Menu()

while is_on: 
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else: 
        #check that we have enough resources for the selected drink with find_drink(order_name) method
        drink = menu.find_drink(choice)
        #print(drink)
        # print(coffee_maker.is_resource_sufficient(drink))

        #Combine our two if statements into a single check with AND
        # if coffee_maker.is_resource_sufficient(drink):
        #     if money_machine.make_payment(drink.cost): #return true if payment successful
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            """Make the coffee """
            coffee_maker.make_coffee(drink)