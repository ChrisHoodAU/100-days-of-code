from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# coffee = CoffeeMaker()
# menu = Menu()
# money = MoneyMachine()
# menu_item = MenuItem()
# coffee.report()
# menu.get_items()

# should_continue = True

# while should_continue:
#     selection = input(" What would you like? (espresso/latte/cappuccino): ").lower()
#     if selection == 'off':
#         should_continue = False
#     elif selection == 'report':
#         coffee.report()
#         money.report()
#     elif menu.find_drink(selection):
#         if coffee.is_resource_sufficient(selection): #stuck here getting menu items
#             money.process_coins()
#             money.make_payment(Menu)
#             coffee.make_coffee(selection) # also here

###################

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True



while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})? ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost): #you don't need to process the coins yourself, the class does
            coffee_maker.make_coffee(drink)
